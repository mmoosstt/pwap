from pydantic import BaseModel
from typing import List
from uuid import UUID, uuid4
from datetime  import datetime

# school:{id:0, type:"school", name:"defaultSchool", changeDate: moment().format()},
class School(BaseModel):
    id:UUID = UUID('00000000-0000-0000-0000-000000000000')
    type:str="school"
    name:str="<insert>"
    changeDate:datetime  = datetime.now()

class Schools(BaseModel):
    items:List[School] = []