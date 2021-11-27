# -*- mode: python -*-
import PySide2
pathPySide2 = PySide2.__path__[0]
import docx
pathDoc = docx.__file__.replace("\\__init__.py", "")

import os


block_cipher = None
#spos\\ui\\webapp\\dist

a = Analysis(['..\\lib\\main.py'],
             pathex=['..\\lib'],
             binaries=[],
             datas=[
                 ("{}\\QtWebEngineProcess.exe".format(pathPySide2), ".\\PySide2"),
                 ("{}\\Qt5PrintSupport.dll".format(pathPySide2), ".\\PySide2"),
                 ("{}\\Qt5Core.dll".format(pathPySide2), ".\\PySide2"),
                 ("{}\\Qt5Gui.dll".format(pathPySide2), ".\\PySide2"),
                 ("{}\\Qt5Network.dll".format(pathPySide2), ".\\PySide2"),
                 ("{}\\Qt5WebChannel.dll".format(pathPySide2), ".\\PySide2"),
                 ("{}\\Qt5WebEngineCore.dll".format(pathPySide2), ".\\PySide2"),
                 ("{}\\Qt5WebEngine.dll".format(pathPySide2), ".\\PySide2"),
                 ("{}\\resources".format(pathPySide2), ".\\PySide2\\resources"),
                 ("{}\\translations".format(pathPySide2), ".\\PySide2\\translations"),
                 ("{}\\spos\\ui\\webapp\\dist".format("..\\lib"), ".\\spos\\ui\\webapp\\dist"),
				 ("{}\\templates".format(pathDoc), "docx\\templates")],
             hiddenimports=['PySide2.QtPrintSupport',
                'PySide2.QtCore',
                'PySide2.QtGui',
                'PySide2.QtNetwork',
                'PySide2.QtWebChannel',
                'PySide2.QtWebEngineCore',
                'PySide2.QtWebEngine',
                'uvicorn.logging',
                'uvicorn.loops',
                'uvicorn.loops.auto',
                'uvicorn.protocols',
                'uvicorn.protocols.http',
                'uvicorn.protocols.http.auto',
                'uvicorn.protocols.websockets',
                'uvicorn.protocols.websockets.auto',
                'uvicorn.lifespan',
                'uvicorn.lifespan.on',
				'pony.orm.dbproviders',
				'pony.orm.dbproviders.sqlite',
                'spos.api',
                'spos.api.pupil',
				'spos.api.pupilvaluation',
				'spos.api.pupilvaluationset',
				'spos.api.school',
				'spos.api.schoolclass',
				'spos.api.valuation',
				'spos.api.valuationdetail',
				'spos.api.setup',
                'spos.ui.webapp',
                'spos.ui.webapp.vue'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='SPOS',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )

