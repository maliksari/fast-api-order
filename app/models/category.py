from sqlmodel import Field, Relationship
from typing import List

from .product import Product
from .base import BaseModel
from .product import CategoryProduct


class Category(BaseModel, table=True):
    __tablename__ = "categories"
    name: str = Field(max_length=150, nullable=False, index=True)
    category_code: str = Field(max_length=150, nullable=False, unique=True)
    list_order: int = None
    products: List[Product] = Relationship(
        back_populates='categories', link_model=CategoryProduct)

