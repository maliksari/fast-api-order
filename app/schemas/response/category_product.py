from pydantic import BaseModel
from typing import List,Optional

from app.schemas.response.product import ProductResponse


class CategoryProductsResponse(BaseModel):
    name: str
    category_code: str
    list_order: int
    products: Optional[List[ProductResponse]]

    class Config:
        orm_mode = True
