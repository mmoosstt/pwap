import os
import sys
import subprocess
import shutil
import zipfile

shutil.rmtree(".\\dist", True)

root_path = __file__[:__file__.rfind('\\')]

python_path = sys.exec_prefix
cmd = "{python_path}\\Scripts\\pyinstaller.exe SposOneFile.spec -y".format(
    python_path=python_path)

_ret = subprocess.Popen(cmd, shell=False, cwd=root_path)
_ret.wait()

if 0:
    print("zip")
    
    def zipfolder(foldername, target_dir):            
        zipobj = zipfile.ZipFile(foldername + '.zip', 'w', zipfile.ZIP_DEFLATED)
        rootlen = len(target_dir) + 1
        for base, dirs, files in os.walk(target_dir):
            for file in files:
                fn = os.path.join(base, file)
                zipobj.write(fn, fn[rootlen:])
    
    zipfolder('./spos.zip', './dist') 
    
    print("done")