from fastapi import APIRouter
from spos.api.pupil import dto
from spos.storage.db.pupil import glue
from uuid import UUID

router = APIRouter()

@router.get(f"/all", response_model = dto.Pupils)
def getAll():
    return glue.load()

@router.get(f"/default", response_model = dto.Pupil)
def getDefault():
    return dto.Pupil()

@router.put("/", response_model = dto.Pupil)
def put(pupil:dto.Pupil):
    glue.save(pupil)
    return pupil

@router.delete("/", response_model = bool)
def delete(pupilId:UUID):
    return glue.delete(pupilId)