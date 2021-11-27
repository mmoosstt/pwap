from fastapi import APIRouter
from spos.api.valuationdetailtext import dto
from spos.storage.db.valuationdetailtext import glue
from uuid import UUID

router = APIRouter()

@router.get(f"/all", response_model = dto.ValuationDetailTexts)
def getAll():
    return glue.load()

@router.get(f"/default", response_model = dto.ValuationDetailText)
def getDefault():
    return dto.ValuationDetailText()

@router.put("/", response_model = dto.ValuationDetailText)
def put(valuationDetail:dto.ValuationDetailText):
    glue.save(valuationDetail)
    return valuationDetail

@router.delete("/", response_model = bool)
def delete(ValuationDetailTextId:UUID):
    return glue.delete(ValuationDetailTextId)