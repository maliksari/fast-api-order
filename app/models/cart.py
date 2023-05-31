from sqlmodel import Field
from typing import Optional
from decimal import Decimal


from .base import BaseModel
from .users import User


class Cart(BaseModel, table=True):
    __tablename__ = "carts"
    user_id: int = Field(default=None, foreign_key="users.id")
    total_price: Decimal = Field(default=None, nullable=True)
    is_completed: bool = Field(default=False, nullable=False)


class CartItem(BaseModel, table=True):
    __tablename__ = "cart_item"
    cart_id: int = Field(default=None, foreign_key="carts.id")
    product_id: int = Field(default=None, foreign_key="products.id")
    quantity:int = Field(default=None,nullable=False)
    item_price:Decimal = Field(default=None, nullable=False)
