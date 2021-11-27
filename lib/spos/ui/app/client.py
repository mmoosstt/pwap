import sys
import asyncio

from PySide2 import QtCore, QtWebEngineWidgets, QtWidgets
from spos.storage.db.setup import setupDatabase
from spos.config import config, report
import PySide2

class Switch(QtCore.QObject):
    sWrite = QtCore.Signal(str)
    
    def __init__(self, stream):
        QtCore.QObject.__init__(self)
        self.stream = stream
            
    def read(self):
        return self.stream.read()
    
    def write(self, value):
        self.sWrite.emit(value.replace("\n", ""))
        return self.stream.write(value)
    
    def flush(self):
        return self.stream.flush()
    
    def isatty(self):
        return self.stream.isatty()
        

sys.stdout = Switch(sys.stdout)
sys.stderr = Switch(sys.stderr)

class ReloadDataBase(QtWidgets.QWidget):

    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.parent = parent
        self.btnSelectDb = QtWidgets.QPushButton(self)
        self.btnSelectDb.setText("select database")
        self.btnSelectDb.pressed.connect(self.slotSelectDb)

        self.btnReloadDb = QtWidgets.QPushButton(self)
        self.btnReloadDb.setText("reload")
        self.btnReloadDb.pressed.connect(self.slotReload)

        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.btnSelectDb)
        layout.addWidget(self.btnReloadDb)
        
        self.dialog = QtWidgets.QFileDialog(self)                        
        layout.addWidget(self.dialog)
        
        self.setLayout(layout)
        
    def slotSelectDb(self):
        _path, __ = self.dialog.getSaveFileName(parent = self.parent,
                                    caption="", 
                                    dir=config["database"], 
                                    filter="*.sqlite")

        if _path != "":
            setupDatabase(_path)
            
        self.slotReload()
        
    def slotReload(self):
        self.parent.web_view.reload()
        
        
class WebEnginePage(QtWebEngineWidgets.QWebEnginePage):
    
    def __init__(self, *args, **kwargs):
        QtWebEngineWidgets.QWebEnginePage.__init__(self, *args, **kwargs)
        self.profile().downloadRequested.connect(self.on_down)

    def on_down(self, download):
        _filter="DOCX (*.docx)"
        _caption="savefile"
        _dir=f"{download.downloadDirectory()}\\{download.downloadFileName()}"
        _options=None
        _filepath, _filter_selected = QtWidgets.QFileDialog.getSaveFileName(None, _caption, _dir, _filter, _options)
    
        if (_filter == _filter_selected):
            _pos = _filepath.rfind("/")
    
            _path = _filepath[:_pos]
            _name = _filepath[_pos+1:]
            
            download.setDownloadDirectory(_path)
            download.setDownloadFileName(_name)
            
        return download.accept()
        
        
        
    def javaScriptConsoleMessage(self, *args, **kwargs):
        print("java", args)
        return QtWebEngineWidgets.QWebEnginePage.javaScriptConsoleMessage(self, *args, **kwargs)
        
    def download(self, *args, **kwargs):
        print("download", args)
        return QtWebEngineWidgets.QWebEnginePage.download(self, *args, **kwargs)
        
    
class MainWindow(QtWidgets.QWidget):
    def __init__(self, port, servers):
        QtWidgets.QWidget.__init__(self, parent=None)
        self.servers = servers
      
        
        self.web_view  = QtWebEngineWidgets.QWebEngineView()
        self.page = WebEnginePage(self.web_view)
        self.web_view.setPage(self.page)
        
        url = 'http://localhost:{}/webapp/index.html'.format(port)
        print(url)
        
        self.web_view.setUrl(QtCore.QUrl(url))
        self.web_view.loadStarted.connect(lambda: print("started"))
        self.web_view.loadFinished.connect(lambda: print("finished"))
        self.stdOut = QtWidgets.QPlainTextEdit()
        self.stdOut.setGeometry(QtCore.QRect(0, 0, 521, 81))
        self.stdOut.setObjectName("stdOut")
        self.stdOut.setMaximumBlockCount(1000)

        self.stdErr = QtWidgets.QPlainTextEdit()
        self.stdErr.setGeometry(QtCore.QRect(0, 0, 521, 81))
        self.stdErr.setObjectName("stdErr")
        self.stdErr.setMaximumBlockCount(1000)
        
        self.btn = QtWidgets.QPushButton()
        self.btn.setMaximumHeight(15)
        self.btn.setMaximumWidth(15)
        self.layoutBtn = QtWidgets.QVBoxLayout()
        self.layoutBtn.addStretch(0)
        self.layoutBtn.addWidget(self.btn)
        
        self.btnDb = ReloadDataBase(self)
                
        self.hide = True
        self.stdErr.hide()
        self.stdOut.hide()
        self.btnDb.hide()
        
        def hideSwitch():
            if self.hide:
                self.stdErr.show()
                self.stdOut.show()
                self.btnDb.show()
                self.hide = False
            else:
                self.stdErr.hide()
                self.stdOut.hide()
                self.btnDb.hide()
                self.hide = True
                
        self.btn.clicked.connect(hideSwitch)
        
        self.layoutH = QtWidgets.QHBoxLayout()
        
        self.layoutH.addLayout(self.layoutBtn)
        self.layoutH.addStretch(0)
        self.layoutH.addWidget(self.stdOut, stretch=1)
        self.layoutH.addWidget(self.stdErr, stretch=1)
        self.layoutH.addWidget(self.btnDb)
                
        sys.stdout.sWrite.connect(self.stdOut.appendPlainText)
        sys.stderr.sWrite.connect(self.stdErr.appendPlainText)
        
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.web_view, stretch=1000)
        layout.addLayout(self.layoutH)
        layout.activate()
        
        self.setWindowTitle("SPOS v0.0.1")
        self.setLayout(layout)
        self.showMaximized()

    def on_downloadRequested(self, u):
        print("alsdfjl", u)
        
    async def shutdown(self, server):
        return await server.shutdown()

    def closeEvent(self, *args, **kwargs):
        _return = QtWidgets.QWidget.closeEvent(self, *args, **kwargs)
        
        for server in self.servers:
            asyncio.ensure_future(self.shutdown(server))
            
        return _return

async def qt_loop(port, loop):   
    
    app = QtWidgets.QApplication(sys.argv)
    wb = MainWindow(port, loop)
    report()
   
    while True:
        app.processEvents()
        await asyncio.sleep(0.0005)



