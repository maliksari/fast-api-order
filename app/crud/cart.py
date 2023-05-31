from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from starlette import status
from datetime import datetime
from starlette.responses import JSONResponse


class CartRepository:
    def __init__(self, db: AsyncSession, model):
        self.db = db
        self.model = model
    
    async def create_cart():
        pass