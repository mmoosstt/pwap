from datetime import datetime
from pony.orm import PrimaryKey, Required, Set
from uuid import UUID, uuid4
from spos.storage.db import util
   
    
class ValuationDetailText(util.DbManager.db().Entity):
    id = PrimaryKey(UUID, auto=True, default=uuid4)
    text = Required(str)
    valuationDetail = Required("ValuationDetail", reverse="gradeTexts")
    