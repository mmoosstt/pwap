from datetime import datetime
from decimal import Decimal
from pony.orm import Database, PrimaryKey, Required, sql_debug
from uuid import UUID, uuid4

class DbManager(object):
    
    _db = None
    
    @classmethod
    def db(cls):
        if cls._db == None:
            cls._db = Database()
            sql_debug(True)
            
        return cls._db

    
