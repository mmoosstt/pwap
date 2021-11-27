from spos.api.pupilvaluationset import dto
from spos.storage.db.pupilvaluationset import orm as ormPVS
from spos.storage.db.pupilvaluation import orm as ormPV
from spos.storage.db.pupil import orm as ormP
from pony.orm import db_session
from datetime import datetime

@db_session
def save(dto:dto.PupilValuationSet):  
    _orm = ormPVS.PupilValuationSet.get(id=dto.id)
    pupil = ormP.Pupil.get(id=dto.pupilId)
    if _orm is None:
        _orm = ormPVS.PupilValuationSet(id=dto.id,
                             pupil = pupil,
                             name=dto.name,
                             changeDate=dto.changeDate)
    else:
        _orm.set(id=dto.id,
             pupil = pupil,
             name=dto.name,
             changeDate=datetime.now())
    
        
@db_session
def delete(uuid):
    _pvs = ormPVS.PupilValuationSet.get(id=uuid)
    if not (_pvs is None):
        for _pv in _pvs.pupilValuations:
            _pv.delete()
        _pvs.delete()
        return True
    
    return False

@db_session
def load():
    _dtos = dto.PupilValuationSets()
    for _db in ormPVS.PupilValuationSet.select():
        _dto = dto.PupilValuationSet()
        _dto.id = _db.id
        _dto.pupilId = _db.pupil.id
        _dto.name = _db.name
        _dto.changeDate = _db.changeDate
        
        _dtos.items.append(_dto)
        
    return _dtos
