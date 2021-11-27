from pydantic import BaseModel
from typing import List
from uuid import UUID, uuid4
from datetime  import datetime

# pupil:{id:0, type:"pupil", schoolClassId:0,  name:"givenName", familyName:"familyName", givenName:"givenName", changeDate: moment().format()}
class Pupil(BaseModel):
    id:UUID = UUID('00000000-0000-0000-0000-000000000000')
    schoolClassId:UUID = UUID('00000000-0000-0000-0000-000000000000')
    type:str="pupil"
    name:str="<insert>"
    familyName:str="<insert>"
    givenName:str="<insert>"
    changeDate:datetime = datetime.now()

class Pupils(BaseModel):
    items:List[Pupil] = []