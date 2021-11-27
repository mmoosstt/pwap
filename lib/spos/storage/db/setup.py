import traceback
import time
import imp
import sys
import os

from spos.storage.db.util import DbManager
from spos.storage.db.pupil import orm as ormP
from spos.storage.db.schoolclass import orm as ormSC
from spos.storage.db.school import orm as ormS
from spos.storage.db.pupilvaluationset import orm as ormPVS
from spos.storage.db.pupilvaluation import orm as ormPV
from spos.storage.db.valuation import orm as ormV
from spos.storage.db.valuationdetail import orm as ormVD
from spos.storage.db.valuationdetailtext import orm as ormVDT

def setupDatabase(filepath = None):
    
    # spos variant dir variant
    if filepath is None:
        
        if sys.path[0].lower().rfind("\\spos") > 0:
            _sub = sys.path[0][:sys.path[0].lower().rfind("\\spos")]
            filepath = "{}\\test.sqlite".format(_sub)  
           
        # single file variant
        elif sys.path[0].lower().rfind("\\_mei")>0:
            _sub = sys.path[0][:sys.path[0].lower().rfind("\\_mei")]
            filepath = "{}\\test.sqlite".format(_sub)
            
        else:
            raise "path error"
            
    if DbManager.db() != None:
        DbManager._db.disconnect()
        DbManager._db = None
        
        imp.reload(ormP)
        imp.reload(ormSC)
        imp.reload(ormS)
        imp.reload(ormPVS)
        imp.reload(ormPV)
        imp.reload(ormV)
        imp.reload(ormVD)
        imp.reload(ormVDT)
    
    DbManager.db().bind(provider='sqlite', filename=filepath, create_db=True)
    DbManager.db().generate_mapping(create_tables=True)