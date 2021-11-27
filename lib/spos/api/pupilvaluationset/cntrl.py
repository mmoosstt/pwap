from fastapi import APIRouter
from spos.api.pupilvaluationset  import dto
from spos.storage.db.pupilvaluationset import glue
from uuid import UUID

router = APIRouter()

@router.get(f"/all", response_model = dto.PupilValuationSets)
def getAll():
    return glue.load()

@router.get(f"/default", response_model = dto.PupilValuationSet)
def getDefault():
    return dto.PupilValuationSet()

@router.put("/", response_model = dto.PupilValuationSet)
def put(pupilvaluationset:dto.PupilValuationSet):
    glue.save(pupilvaluationset)
    return pupilvaluationset

@router.delete("/", response_model = bool)
def delete(pupilValuationSetId:UUID):
    glue.delete(pupilValuationSetId)
    return True