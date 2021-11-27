import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRoute
from starlette.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from spos.ui import webapp

from spos.api.pupil import cntrl as PupilCntrl
from spos.api.pupilvaluation import cntrl as PupilValuationCntrl
from spos.api.pupilvaluationset import cntrl as PupilValuationSetCntrl
from spos.api.school import cntrl as SchoolCntrl
from spos.api.schoolclass import cntrl as SchoolClassCntrl
from spos.api.valuation import cntrl as ValuationCntrl
from spos.api.valuationdetail import cntrl as ValuationDetailCntrl
from spos.api.valuationdetailtext import cntrl as ValuationDetailTextCntrl

from spos.api.report import cntrl as ReportCntrl
from spos.config import config

app = FastAPI( title="SPOS",
    description="TBD",
    version="0.0.1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=("*", "http://localhost:*/",),
    allow_methods=("DELETE", "GET", "POST", "PUT",),
    allow_headers=("*",),
    allow_credentials=True,
)

#{config['reports']}

app.mount("/webapp", StaticFiles(directory="{}\\dist".format(webapp.__path__[0])), name="Spos")
app.mount("/report", StaticFiles(directory=f"{config['reports']}"), name="Path")

app.include_router(PupilCntrl.router, prefix="/spos/pupil", tags=["Pupil"])
app.include_router(PupilValuationCntrl.router, prefix="/spos/pupilvaluation", tags=["PupilValuation"])
app.include_router(PupilValuationSetCntrl.router, prefix="/spos/pupilvaluationset", tags=["PupilValuationSet"])
app.include_router(SchoolCntrl.router, prefix="/spos/school", tags=["School"])
app.include_router(SchoolClassCntrl.router, prefix="/spos/schoolclass", tags=["SchoolClass"])
app.include_router(ValuationCntrl.router, prefix="/spos/valuation", tags=["Valuation"])
app.include_router(ValuationDetailCntrl.router, prefix="/spos/valuationdetail", tags=["ValuationDetail"])
app.include_router(ReportCntrl.router, prefix="/spos/report", tags=["Report"])
app.include_router(ValuationDetailTextCntrl.router, prefix="/spos/valuationdetailtext", tags=["ValuationDetailText"])

# handling fastapi <-> openapi-generate !!!
def setup_openapi(app: FastAPI) -> None:
    """
    Simplify operation IDs so that generated clients have simpler api function names.

    Should be called on a FastAPI instance only after all routes have been added.
    """
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name
            
setup_openapi(app)

def run_server():
    uvicorn.run("spos.server.server:app", host="127.0.0.1", port=5001, log_level="info")
