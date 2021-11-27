from datetime import datetime
from pony.orm import PrimaryKey, Required, Set, composite_key
from uuid import UUID, uuid4
from spos.storage.db import util

class PupilValuation(util.DbManager.db().Entity):
    id = PrimaryKey(UUID, auto=True, default=uuid4)
    pupilValuationSet = Required("PupilValuationSet")
    valuation = Required("Valuation")
    composite_key(pupilValuationSet, valuation)
    
    name=Required(str)
    grade=Required(int)
    gradeText=Required(str)
    changeDate = Required(datetime, default=datetime.now)