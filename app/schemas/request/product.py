from pydantic import BaseModel
from typing import Optional


class ProductRequest(BaseModel):
    name: str
    product_code: str
    price: Optional[float]
    description: str
    list_order: int
    stock_amount: int
