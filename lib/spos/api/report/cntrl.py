from fastapi import APIRouter, File
from spos.storage.db.pupil import glue
from uuid import UUID
from spos.config import config
from starlette.responses import FileResponse, StreamingResponse
from spos.domain.report import Reports

router = APIRouter()
reports = Reports()

@router.get(f"/pupil", response_class = StreamingResponse)
def requestPupilReport(pupilId:UUID):
    return StreamingResponse(reports.reportPupil(pupilId), media_type="application/doc")

@router.get(f"/schoolclass", response_class = FileResponse)
def requestSchoolClassReport(schoolClassId:UUID):
    return StreamingResponse(reports.reportSchoolClass(schoolClassId), media_type="application/doc")

