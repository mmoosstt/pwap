from pydantic import BaseModel
from typing import List
from uuid import UUID
from datetime  import datetime

# valuationDetail:{id:0, type:"valuationDetail", valuationId:0, grade:-1, gradeTexts:[], changeDate: moment().format()}
class ValuationDetailText(BaseModel):
    id:UUID = UUID('00000000-0000-0000-0000-000000000000')
    type:str="valuationDetailText"
    text:str="valuationDetail"
    valuationDetailId:UUID = UUID('00000000-0000-0000-0000-000000000000')
    

class ValuationDetailTexts(BaseModel):
    items:List[ValuationDetailText] = []