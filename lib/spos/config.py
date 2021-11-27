import json
import sys
import os 
from datetime import datetime

#spos local
if sys.path[0].lower().rfind("\\pwap") > 0:
    path = sys.path[0][:sys.path[0].lower().rfind("\\pwap")]
    filepathConfig = f"{path}\\pwap\\spos-config.json"
    filepathDB = f"{path}\\pwap\\spos-db.sqlite"
    folderReports = f"{path}\\reports"
   
#spos single file exe
elif sys.path[0].lower().rfind("\\_mei") > 0:
    path = sys.path[0][:sys.path[0].lower().rfind("\\_mei")]
    filepathConfig = f"{path}\\spos-config.json"
    filepathDB = f"{path}\\spos-db.sqlite"
    folderReports = f"{path}\\reports"
            
template = {"version":0,
            "host":"localhost",
            "port":None,
            "database":filepathDB,
            "config":filepathConfig,
            "reports":folderReports}

def createConfig():
    with open(filepathConfig,"w") as f:
        json.dump(template, f)
        
# create config file from template
if not os.path.isfile(filepathConfig):
    createConfig()

config = None
with open(filepathConfig, "r") as f:  
    config = json.load(f)

if not os.path.exists(config['reports']):
    os.mkdir(config['reports'])
        
def report():
    print(f"{sys.path[0]}Config:")
    for key in config:
        print(f"\t{key}: {config[key]}")