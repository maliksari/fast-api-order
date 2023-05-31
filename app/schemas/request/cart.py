from pydantic import BaseModel
from typing import Optional

class CartRequest(BaseModel):
    quantity:int
    product_id:int
