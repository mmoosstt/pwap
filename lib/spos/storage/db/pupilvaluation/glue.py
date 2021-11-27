from spos.api.pupilvaluation import dto
from spos.storage.db.pupilvaluation import orm
from spos.storage.db.pupilvaluationset import orm as ormPVS
from spos.storage.db.valuation import orm as ormV
from pony.orm import db_session, select
from datetime import datetime


@db_session
def save(dto:dto.PupilValuation):  
    _orm = orm.PupilValuation.get(id=dto.id)
    _pvs = ormPVS.PupilValuationSet.get(id=dto.pupilValuationSetId)
    _v = ormV.Valuation.get(id=dto.valuationId)

    if dto.gradeText.strip():
        if _orm is None:
            _orm = orm.PupilValuation(id=dto.id,
                                 valuation = _v,
                                 pupilValuationSet = _pvs,
                                 name=dto.name,
                                 grade= dto.grade,
                                 gradeText = dto.gradeText.strip(),
                                 changeDate=dto.changeDate)
        else:       
            _orm.set(id=dto.id,
                     valuation = _v,
                     pupilValuationSet = _pvs,
                     name=dto.name,
                     grade= dto.grade,
                     gradeText = dto.gradeText.strip(),
                     changeDate=datetime.now())
    
        
@db_session
def delete(uuid):
    _orm = orm.PupilValuation.get(id=uuid)
    if not (_orm is None):
        _orm.delete()
        return True
    
    return False

@db_session
def load():
    _dtos = dto.PupilValuations()
    for _db in orm.PupilValuation.select():
        _dto = dto.PupilValuation()
        _dto.id = _db.id
        _dto.pupilValuationSetId = _db.pupilValuationSet.id
        _dto.valuationId = _db.valuation.id
        _dto.name = _db.name
        _dto.grade = _db.grade
        _dto.gradeText = _db.gradeText
        _dto.changeDate = _db.changeDate
        
        _dtos.items.append(_dto)
        
    return _dtos
