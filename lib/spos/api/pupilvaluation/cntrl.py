from fastapi import APIRouter
from spos.api.pupilvaluation import dto
from spos.storage.db.pupilvaluation import glue
from uuid import UUID
from spos.api import pupil

router = APIRouter()

@router.get(f"/all", response_model = dto.PupilValuations)
def getAll():
    return glue.load()

@router.get(f"/default", response_model = dto.PupilValuation)
def getDefault():
    return dto.PupilValuation()

@router.put("/", response_model = dto.PupilValuation)
def put(pupilvaluation:dto.PupilValuation):
    glue.save(pupilvaluation)
    return pupilvaluation

@router.delete("/", response_model = bool)
def delete(pupilValuationId:UUID):
    glue.delete(pupilValuationId)
    return True