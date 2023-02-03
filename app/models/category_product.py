# from sqlmodel import Field, SQLModel, Relationship
# from typing import Optional, List

# from .base import BaseModel
# from .product import Product


# class CategoryProduct(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
#     product_id: int = Field(default=None, foreign_key="product.id")
#     category_id: int = Field(default=None, foreign_key="category.id")



# class Category(BaseModel, table=True):
#     name: str = Field(max_length=150, nullable=False, index=True)
#     category_code: str = Field(max_length=150, nullable=False, unique=True)
#     list_order: int = None
#     category_product_id: List[Product] = Relationship(
#         back_populates='products', link_model=CategoryProduct)



