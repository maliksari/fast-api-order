from typing import Optional

from pydantic import BaseModel


class ResponseUser(BaseModel):
    id: Optional[int]  
    username: str 
    name: str 
    surname: str 
    age: int
   
    