from spos.api.pupil import dto
from spos.storage.db.pupil import orm
from spos.storage.db.schoolclass import orm as ormSC
from pony.orm import db_session
from datetime import datetime

@db_session
def save(pupilDto:dto.Pupil):
    
    pupil = orm.Pupil.get(id=pupilDto.id)
    schoolclass = ormSC.SchoolClass.get(id=pupilDto.schoolClassId)
    
    if pupil is None:
        # create
        pupil = orm.Pupil(id=pupilDto.id,
                             schoolClass=schoolclass,
                             name=pupilDto.name,
                             familyName=pupilDto.familyName,
                             givenName=pupilDto.givenName,
                             changeDate=pupilDto.changeDate)
    else:
        # update
        pupil.set(id=pupilDto.id,
                             schoolClass=schoolclass,
                             name=pupilDto.name,
                             familyName=pupilDto.familyName,
                             givenName=pupilDto.givenName,
                             changeDate=datetime.now())
    
        
@db_session
def delete(uuid):
    p = orm.Pupil.get(id=uuid)
    if not (p is None):
        for pvs in p.pupilValuationSets:
            for pv in pvs.pupilValuations:
                pv.delete()
            pvs.delete()
        p.delete()
        return True
    
    return False

@db_session
def load():
    _dtos = dto.Pupils()
    for _db in orm.Pupil.select():
        
        _dto = dto.Pupil()
        _dto.id = _db.id
        _dto.schoolClassId = _db.schoolClass.id
        _dto.familyName = _db.familyName
        _dto.givenName = _db.givenName
        _dto.changeDate = _db.changeDate
        
        _dtos.items.append(_dto)
        
    return _dtos
