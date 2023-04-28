from pydantic import BaseModel


class CategoryRequest(BaseModel):
    name: str
    category_code: str
    list_order: int

