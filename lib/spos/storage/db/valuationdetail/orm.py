from datetime import datetime
from pony.orm import PrimaryKey, Required, Set
from uuid import UUID, uuid4
from spos.storage.db import util

class ValuationDetail(util.DbManager.db().Entity):
    id = PrimaryKey(UUID, auto=True, default=uuid4)
    valuation = Required("Valuation")
    name=Required(str)
    grade=Required(int)
    changeDate = Required(datetime, default=datetime.now)
    gradeTexts=Set("ValuationDetailText")
    