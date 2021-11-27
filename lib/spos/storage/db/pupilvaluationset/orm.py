from datetime import datetime
from pony.orm import PrimaryKey, Required, Set
from uuid import UUID, uuid4
from spos.storage.db import util

class PupilValuationSet(util.DbManager.db().Entity):
    id = PrimaryKey(UUID, auto=True, default=uuid4)
    pupil = Required("Pupil")
    pupilValuations = Set("PupilValuation")
    name=Required(str)
    changeDate = Required(datetime, default=datetime.now)
    