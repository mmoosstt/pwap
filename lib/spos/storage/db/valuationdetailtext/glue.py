from spos.api.valuationdetailtext import dto
from spos.storage.db.valuationdetailtext import orm
from spos.storage.db.valuationdetail import orm as ormVD
from pony.orm import db_session
from uuid import uuid4, UUID

@db_session
def save(dto:dto.ValuationDetailText):  
    _ormVD = ormVD.ValuationDetail.get(id=dto.valuationDetailId)
    _orm = orm.ValuationDetailText.get(id=dto.id)
    
    if (_ormVD != None) and (_orm == None):
        _orm = orm.ValuationDetailText(id=uuid4(),
                                       text=dto.text,
                                       valuationDetail=_ormVD)
        
    elif (_ormVD != None) and (_orm != None):
        _orm.set(id=dto.id,
                 text=dto.text,
                 valuationDetail=_ormVD)
                        
@db_session
def delete(uuid:UUID):
    _orm = orm.ValuationDetailText.get(id=uuid)
    if not(_orm is None):
        _orm.delete()
        return True
    
    return False        

@db_session
def load():
    _dtos = dto.ValuationDetailTexts()
    for _db in orm.ValuationDetailText.select():
        _dto = dto.ValuationDetailText(id=_db.id,
                                       text=_db.text,
                                       valuationDetailId=_db.valuationDetail.id)
        
        _dtos.items.append(_dto)
        
    return _dtos
