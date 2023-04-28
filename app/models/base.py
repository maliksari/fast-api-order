from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field
from sqlalchemy.sql import func
from sqlalchemy import Column, DateTime


class BaseModel(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    is_active: bool = True
    created_at:  Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now())
    )
    created_by: Optional[int] = Field(
        default=None, foreign_key="users.id"
    )
    modified_at: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True), onupdate=func.now())
    )

    modified_by: Optional[int] = Field(
        default=None, foreign_key="users.id"
    )
