from spos.api.valuationdetail import dto
from spos.storage.db.valuationdetail import orm
from spos.storage.db.valuationdetailtext import orm as ormVDT
from spos.storage.db.valuation import orm as ormV
from pony.orm import db_session
from datetime import datetime
from uuid import uuid4, UUID

@db_session
def save(dto:dto.ValuationDetail):  
    _orm = orm.ValuationDetail.get(id=dto.id)
    _ormV = ormV.Valuation.get(id=dto.valuationId)
    if _orm is None:
        _orm = orm.ValuationDetail(id=uuid4(),
                                   valuation = _ormV,
                                   name=dto.name,
                                   grade = dto.grade,
                                   changeDate=dto.changeDate)

    else:
        _orm.set(id=dto.id,
               valuation = _ormV,
               name=dto.name,
               grade = dto.grade,
               changeDate=datetime.now())
    
    for _gradeText in dto.gradeTexts:
        if _gradeText.strip():
            _ormVDT = ormVDT.ValuationDetailText.get(text=_gradeText.strip())
            if _ormVDT is None:
                _ormVDT = ormVDT.ValuationDetailText(id=uuid4(),
                                              text=_gradeText.strip(),
                                              valuationDetail=_orm)
                        
@db_session
def delete(uuid:UUID):
    _orm = orm.ValuationDetail.get(id=uuid)
    if not (_orm is None):
        _orm.delete()
        return True
    
    return False

@db_session
def load():
    
    _dtos = dto.ValuationDetails()
    for _db in orm.ValuationDetail.select():
        
        _valuationTexts = []
        for _valuationDetailText in _db.gradeTexts:
            _valuationTexts.append(_valuationDetailText.text)
            
        _dto = dto.ValuationDetail()
        _dto.id = _db.id
        _dto.name = _db.name
        _dto.valuationId = _db.valuation.id
        _dto.grade = _db.grade
        _dto.gradeTexts = _valuationTexts
        _dto.changeDate = _db.changeDate
        _dtos.items.append(_dto)
        
    return _dtos
