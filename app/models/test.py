from sqlmodel import Field

from .base import BaseModel


class Test(BaseModel, table=True):
    name: str = Field(max_length=150, nullable=False)
    test: str
    test2: str = Field(max_length=150, nullable=False)

