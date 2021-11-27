from spos.api.schoolclass import dto
from spos.storage.db.schoolclass import orm
from spos.storage.db.school import orm as ormSchool
from pony.orm import db_session
from datetime import datetime

@db_session
def save(dto:dto.SchoolClass):  
    _orm = orm.SchoolClass.get(id=dto.id)
    _ormSchool = ormSchool.School.get(id=dto.schoolId)
    if _orm is None:
        _orm = orm.SchoolClass(id=dto.id,
                             name=dto.name,
                             school = _ormSchool,
                             changeDate=dto.changeDate)
    else:
        _orm.set(id=dto.id,
                 name=dto.name,
                 changeDate=datetime.now())
    
        
@db_session
def delete(uuid):
    sc = orm.SchoolClass.get(id=uuid)
    if not (sc is None):
        for p in sc.pupils:
            for pvs in p.pupilValuationSets:
                for pv in pvs.pupilValuations:
                    pv.delete()
                pvs.delete()
            p.delete()
        sc.delete()
        return True
    
    return False

@db_session
def load():
    _dtos = dto.SchoolClasses()
    for _db in orm.SchoolClass.select():
        _dto = dto.SchoolClass()
        _dto.id = _db.id
        _dto.schoolId = _db.school.id
        _dto.name = _db.name
        _dto.changeDate = _db.changeDate
        
        _dtos.items.append(_dto)
        
    return _dtos
