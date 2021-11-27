from pydantic import BaseModel
from typing import List
from uuid import UUID
from datetime  import datetime

#pupilValuationSet:{id:0, type:"pupilValuationSet", pupilId:0,  name:"pupilValuationSet", changeDate: moment().format()},
class PupilValuationSet(BaseModel):
    id:UUID = UUID('00000000-0000-0000-0000-000000000000')
    pupilId:UUID = UUID('00000000-0000-0000-0000-000000000000')
    type:str="pupilValuationSet"
    name:str="<insert>"
    changeDate:datetime = datetime.now()

class PupilValuationSets(BaseModel):
    items:List[PupilValuationSet] = []