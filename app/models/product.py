from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List

from .base import BaseModel


class CategoryProduct(BaseModel, table=True):
    __tablename__ = "category_products"
    product_id: int = Field(default=None, foreign_key="products.id")
    category_id: int = Field(default=None, foreign_key="categories.id")


class Product(BaseModel, table=True):
    __tablename__ = "products"
    name: str = Field(max_length=150, nullable=False)
    product_code: str = Field(max_length=150, nullable=False, unique=True)
    price: Optional[float] = Field(description="Ürün fiyatı")
    description: str = Field(max_length=500, default=None)
    list_order: int = Field(description="Liste")
    stock_amount:int = Field(default=0,nullable=False,description="stok miktarı")


    categories: Optional[List["Category"]] = Relationship(
        back_populates="products", link_model=CategoryProduct)
