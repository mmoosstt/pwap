from datetime import datetime
from pony.orm import PrimaryKey, Required, Set
from uuid import UUID, uuid4
from spos.storage.db import util

class SchoolClass(util.DbManager.db().Entity):
    id = PrimaryKey(UUID, auto=True, default=uuid4)
    school = Required("School")
    name=Required(str)
    changeDate = Required(datetime, default=datetime.now)
    pupils = Set("Pupil")