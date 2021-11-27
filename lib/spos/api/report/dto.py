from pydantic import BaseModel
from typing import List
from uuid import UUID
from datetime  import datetime

# valuation:{id:0, type:"valuation", name:"", changeDate: moment().format()},
class FileContainer(BaseModel):
    filename:str="valuation"
    data:bytes=b"<insert>"
    cate:datetime = datetime.now()  
 
