from fastapi import APIRouter
from spos.api.valuationdetail import dto
from spos.storage.db.valuationdetail import glue
from uuid import UUID

router = APIRouter()

@router.get(f"/all", response_model = dto.ValuationDetails)
def getAll():
    return glue.load()

@router.get(f"/default", response_model = dto.ValuationDetail)
def getDefault():
    return dto.ValuationDetail()

@router.put("/", response_model = dto.ValuationDetail)
def put(valuationDetail:dto.ValuationDetail):
    glue.save(valuationDetail)
    return valuationDetail

@router.delete("/", response_model = bool)
def delete(valuationDetailId:UUID):
    return glue.delete(valuationDetailId)