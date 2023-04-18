from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.product import Product
from app.crud.product import ProductRepository
from app.endpoints.auths.auth_handler import get_token_data
from app.schemas.response.product import ProductResponse
from app.schemas.request.product import ProductRequest
from app.settings.database import get_session

router = APIRouter()

@router.get("/",
            tags=["Product"],
            summary="get products",
            response_description="Response ....",
            response_model=List[ProductResponse],
            status_code=status.HTTP_200_OK)
async def get_products(db:AsyncSession= Depends(get_session)):
    products = ProductRepository(db,Product)
    result = await products.get_all()
    return result