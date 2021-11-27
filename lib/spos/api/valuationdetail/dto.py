from pydantic import BaseModel
from typing import List
from uuid import UUID
from datetime  import datetime

# valuationDetail:{id:0, type:"valuationDetail", valuationId:0, grade:-1, gradeTexts:[], changeDate: moment().format()}
class ValuationDetail(BaseModel):
    id:UUID = UUID('00000000-0000-0000-0000-000000000000')
    type:str="valuationDetail"
    name:str="<insert>"
    valuationId:UUID = UUID('00000000-0000-0000-0000-000000000000')
    grade:int=0
    gradeTexts:List[str]=[]
    changeDate:datetime = datetime.now()

class ValuationDetails(BaseModel):
    items:List[ValuationDetail] = []