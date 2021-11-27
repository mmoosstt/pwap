from pydantic import BaseModel
from typing import List
from uuid import UUID, uuid4
from datetime  import datetime

#{"id":"d3755ac5-b7ca-4263-b126-95a25c503f08","type":"school","name":"test","changeDate":"2020-11-22T20:34:23+01:00"}
class SchoolClass(BaseModel):
    id:UUID = UUID('00000000-0000-0000-0000-000000000000')
    schoolId:UUID = UUID('00000000-0000-0000-0000-000000000000')
    type:str="schoolClass"
    name:str="<insert>"
    changeDate:datetime = datetime.now()

class SchoolClasses(BaseModel):
    items:List[SchoolClass] = []