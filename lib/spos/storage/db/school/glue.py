from spos.api.school import dto
from spos.storage.db.school import orm
from pony.orm import db_session
from datetime import datetime

@db_session
def save(dto:dto.School):  
    _orm = orm.School.get(id=dto.id)
    if _orm is None:
        _orm = orm.School(id=dto.id,
                             name=dto.name,
                             changeDate=dto.changeDate)
    else:
        _orm.set(id=dto.id,
                 name=dto.name,
                 changeDate=datetime.now())
    
        
@db_session
def delete(uuid):
    s = orm.School.get(id=uuid)
    if not (s is None):
        for sc in s.schoolClasses:
            for p in sc.pupils:
                for pvs in p.pupilValuationSets:
                    for pv in pvs.pupilValuations:
                        pv.delete()
                    pvs.delete()
                p.delete()
            sc.delete()
        s.delete()
        return True
    
    return False

@db_session
def load():
    _dtos = dto.Schools()
    for _db in orm.School.select():
        _dto = dto.School()
        _dto.id = _db.id
        _dto.name = _db.name
        _dto.changeDate = _db.changeDate
        
        _dtos.items.append(_dto)
        
    return _dtos
