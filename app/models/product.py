from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List

from .base import BaseModel


class CategoryProduct(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    product_id: int = Field(default=None, foreign_key="product.id")
    category_id: int = Field(default=None, foreign_key="category.id")


class Product(BaseModel, table=True):
    name: str = Field(max_length=150, nullable=False)
    product_code: str = Field(max_length=150, nullable=False, unique=True)
    price: Optional[float] = Field(description="Ürün fiyatı")
    description: str = Field(max_length=500, default=None)
    list_order: int = Field(description="Liste")

    categories: Optional[List["Category"]] = Relationship(
        back_populates="products", link_model=CategoryProduct)
