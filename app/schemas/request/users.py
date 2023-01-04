from typing import Optional
from pydantic import validator,BaseModel


class UserCreate(BaseModel):
    username: str 
    name: str 
    surname: str 
    age: Optional[int] 
    password: str
    password2:str

    @validator('password2')
    def password_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError('passwords don\'t match')
        return v


class UserUpdate(BaseModel):
    name: str 
    surname: str 
    age: Optional[int] 