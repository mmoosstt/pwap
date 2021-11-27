from fastapi import APIRouter
from spos.api.school import dto
from spos.storage.db.school import glue
from uuid import UUID

router = APIRouter()

@router.get(f"/all", response_model = dto.Schools)
def getAll():
    return glue.load()

@router.get(f"/default", response_model = dto.School)
def getDefault():
    return dto.School()

@router.put("/", response_model = dto.School)
def put(school:dto.School):
    glue.save(school)
    return school

@router.delete("/", response_model = bool)
def delete(schoolId:UUID):
    return glue.delete(schoolId)