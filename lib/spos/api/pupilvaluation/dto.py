from pydantic import BaseModel
from typing import List
from uuid import UUID
from datetime  import datetime

class PupilValuation(BaseModel):
    id:UUID = UUID('00000000-0000-0000-0000-000000000000')
    pupilValuationSetId:UUID = UUID('00000000-0000-0000-0000-000000000000')
    valuationId:UUID = UUID('00000000-0000-0000-0000-000000000000')
    type:str="pupilValuation"
    name:str="<insert>"
    grade:int=0
    gradeText:str="<insert>"
    changeDate:datetime = datetime.now()

class PupilValuations(BaseModel):
    items:List[PupilValuation] = []