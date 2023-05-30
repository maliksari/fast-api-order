from sqlmodel import Field
from typing import Optional
from decimal import Decimal


from .base import BaseModel
from .users import User


class Cart(BaseModel):
    user_id: int = Field(default=None, foreign_key="user.id")
    total_price: Decimal = Field(default=None, nullable=False)
    is_completed: bool = Field(default=False, nullable=False)


class CartItem(BaseModel):
    cart_id: int = Field(default=None, foreign_key="cart.id")
    product_id: int = Field(default=None, foreign_key="product.id")
    quantity:int = Field(default=None,nullable=False)
    item_price:Decimal = Field(default=None, nullable=False)
