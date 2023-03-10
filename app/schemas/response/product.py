from pydantic import BaseModel
from typing import Optional,List

class ProductResponse (BaseModel):
    name: str
    product_code: str
    price: Optional[float]
    description: str
    list_order: int
    categories: Optional[List]