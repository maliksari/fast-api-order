from pydantic import BaseModel
from typing import Optional


class ProductResponse(BaseModel):
    id: Optional[int] = None
    name: str = ""
    product_code: str = ""
    price: Optional[float] = None
    description: str = ""
    list_order: int = 0
    stock_amount: int = 0

    class Config:
        orm_mode = True
