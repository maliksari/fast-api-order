from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import Field, Session, SQLModel, create_engine, select

from app.models.product import Product, CategoryProduct
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
async def get_products(db: AsyncSession = Depends(get_session)):
    products = ProductRepository(db, Product)
    result = await products.get_all()
    return result


@router.get("/{product_id}", tags=["Product"],
            summary="Product Detail",
            response_description="Response ....",
            response_model=ProductResponse,
            status_code=status.HTTP_200_OK)
async def get_product_detail(product_id: int, db: AsyncSession = Depends(get_session)):
    products = ProductRepository(db, Product)
    result = await products.get_by_id(product_id)
    return result


@router.post("/", tags=["Product"],
             summary="Product create",
             response_description="Response ....",
             response_model=ProductResponse,
             status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductRequest, categories: Optional[List[int]], db: AsyncSession = Depends(get_session), token_data: Any = Depends(get_token_data)):
    created_by_id = token_data["user_id"]
    prod = ProductRepository(db, Product)
    result = await prod.create(product, created_by_id)

    if not categories:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="categories boş birakilamaz !!!")
    try:
        for i in categories:
           
            obj = CategoryProduct(product_id=result.id, category_id=i)
            db.add(obj)
            await db.commit()
            await db.refresh(obj)
    except Exception:
        db.rollback()
        raise Exception("category add product error")
    return result


@router.put("/{product_id}", tags=["Product"],
            summary="Product Detail",
            response_description="Response ....",
            response_model=ProductResponse,
            status_code=status.HTTP_200_OK)
async def update_product(product_id: int, product: ProductRequest, db: AsyncSession = Depends(get_session), token_data: Any = Depends(get_token_data)):
    modified_by_id = token_data["user_id"]
    obj = ProductRepository(db, Product)
    result = await obj.update(product, product_id, modified_by_id)
    return result


@router.delete("/{product_id}",
               tags=["Product"],
               response_description="Deleted product",
               response_model=ProductResponse,
               status_code=status.HTTP_200_OK)
async def deleted(product_id: int, db: AsyncSession = Depends(get_session)):
    obj = ProductRepository(db, Product)
    result = await obj.delete(product_id)
    return result
