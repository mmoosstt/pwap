from datetime import datetime
from pony.orm import PrimaryKey, Optional, Required, Set
from uuid import UUID, uuid4
from spos.storage.db import util


class Pupil(util.DbManager.db().Entity):
    id = PrimaryKey(UUID, auto=True, default=uuid4)
    schoolClass=Optional("SchoolClass")
    name=Required(str)
    familyName=Required(str)
    givenName=Required(str)
    changeDate = Required(datetime, default=datetime.now)
    pupilValuationSets = Set("PupilValuationSet")
    