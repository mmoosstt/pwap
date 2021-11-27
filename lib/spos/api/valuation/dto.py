from pydantic import BaseModel
from typing import List
from uuid import UUID
from datetime  import datetime

# valuation:{id:0, type:"valuation", name:"", changeDate: moment().format()},
class Valuation(BaseModel):
    id:UUID = UUID('00000000-0000-0000-0000-000000000000')
    type:str="valuation"
    name:str="<insert>"
    changeDate:datetime = datetime.now()  
 
class Valuations(BaseModel):
    items:List[Valuation] = []