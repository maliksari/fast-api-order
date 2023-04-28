from pydantic import BaseModel
from typing import Optional


class ProductResponse (BaseModel):
    id: Optional[int]
    name: str
    product_code: str
    price: Optional[float]
    description: str
    list_order: int

    class Config:
        orm_mode = True
