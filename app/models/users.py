from sqlalchemy import Column
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy import Column, DateTime


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    username: str = Field(index=True, max_length=150,
                          unique=True, nullable=False)
    name: str = Field(max_length=150, nullable=False)
    surname: str = Field(max_length=150, nullable=False)
    age: Optional[int] = Field(default=None, nullable=False)
    password: str = Field(max_length=256, min_length=6, nullable=False)
    is_active: bool = Field(default=True)
    created_at:  Optional[datetime] = Field(nullable=True,
                                            sa_column=Column(
                                                DateTime(timezone=True), server_default=func.now())
                                            )
    modified_at: Optional[datetime] = Field(nullable=True,
                                            sa_column=Column(
                                                DateTime(timezone=True), onupdate=func.now()))

