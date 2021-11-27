from pony.orm import db_session
from datetime import datetime
from spos.api.valuation import dto
from spos.storage.db.valuation import orm
from uuid import UUID, uuid4


@db_session
def save(dto:dto.Valuation):  
    _orm = orm.Valuation.get(id=dto.id)
    if _orm is None:
        _orm = orm.Valuation(id=uuid4(),
                             name=dto.name,
                             changeDate=dto.changeDate)
    else:
        _orm.set(id=dto.id,
                 name=dto.name,
                 changeDate=datetime.now())
    
        
@db_session
def delete(uuid:UUID):
    _orm = orm.Valuation.get(id=uuid)
    if not (_orm is None):
        _orm.delete()
        return True
    
    return False

@db_session
def load():
    _dtos = dto.Valuations()
    for _db in orm.Valuation.select():
        _dto = dto.Valuation()
        _dto.id = _db.id
        _dto.name = _db.name
        _dto.changeDate = _db.changeDate
        _dtos.items.append(_dto)
        
    return _dtos
