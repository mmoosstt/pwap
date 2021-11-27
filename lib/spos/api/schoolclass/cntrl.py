from fastapi import APIRouter
from spos.api.schoolclass  import dto
from spos.storage.db.schoolclass import glue
from uuid import UUID

router = APIRouter()

@router.get(f"/all", response_model = dto.SchoolClasses)
def getAll():
    return glue.load()

@router.get(f"/default", response_model = dto.SchoolClass)
def getDefault():
    return dto.SchoolClass()

@router.put("/", response_model = dto.SchoolClass)
def put(schoolclass:dto.SchoolClass):
    glue.save(schoolclass)
    return schoolclass

@router.delete("/", response_model = bool)
def delete(schoolClassId:UUID):
    glue.delete(schoolClassId)
    return True