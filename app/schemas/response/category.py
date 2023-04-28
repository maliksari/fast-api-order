from pydantic import BaseModel
from typing import Optional


class CategoryResponse(BaseModel):
    id: Optional[int]
    name: str
    category_code: str
    list_order: Optional[int]

    class Config:
        orm_mode = True
