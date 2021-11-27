from fastapi import APIRouter
from spos.api.valuation import dto
from spos.storage.db.valuation import glue
from uuid import UUID

router = APIRouter()

@router.get(f"/all", response_model = dto.Valuations)
def getAll():
    return glue.load()

@router.get(f"/default", response_model = dto.Valuation)
def getDefault():
    return dto.Valuation()

@router.put("/", response_model = dto.Valuation)
def put(valuation:dto.Valuation):
    glue.save(valuation)
    return valuation

@router.delete("/", response_model = bool)
def delete(valuationId:UUID):
    glue.delete(valuationId)
    return True