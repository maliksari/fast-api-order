from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.category import Category
from app.crud.category import CategoryRepository
from app.endpoints.auths.auth_handler import get_token_data
from app.schemas.response.category import CategoryResponse
from app.schemas.request.category import CategoryRequest
from app.settings.database import get_session

router = APIRouter()


@router.get("/",
            tags=["Category"],
            summary="get categories",
            response_description="Response ....",
            response_model=List[CategoryResponse],
            status_code=status.HTTP_200_OK)
async def get_categories(db: AsyncSession = Depends(get_session)):
    obj = CategoryRepository(db, Category)
    result = await obj.get_all()
    return result


@router.get("/{category_id}", tags=["Category"],
            summary="get category by id",
            response_description="Response ....",
            response_model=CategoryResponse,
            status_code=status.HTTP_200_OK)
async def get_category_by_id(category_id: int, db: AsyncSession = Depends(get_session)):
    obj = CategoryRepository(db, Category)
    result = await obj.get_by_id(category_id)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category not found with id: {category_id}",
        )

    return result


@router.post("/",
             tags=["Category"],
             response_description="create response",
             response_model=CategoryResponse,
             status_code=status.HTTP_201_CREATED)
async def create_category(category: CategoryRequest, db: AsyncSession = Depends(get_session), token_data: Any = Depends(get_token_data)):
    created_by_id = token_data["user_id"]
    obj = CategoryRepository(db, Category)
    result = await obj.create(category, created_by_id)
    return result


@router.put("/{category_id}",
            tags=["Category"],
            response_description="Update",
            response_model=CategoryResponse,
            status_code=status.HTTP_200_OK)
async def update(category_id: int, category: CategoryRequest, db: AsyncSession = Depends(get_session), token_data: Any = Depends(get_token_data)):
    modified_by_id = token_data["user_id"]
    obj = CategoryRepository(db, Category)
    result = await obj.update(category, category_id, modified_by_id)
    return result


@router.delete("/{category_id}",
               tags=["Category"],
               response_description="Deleted category",
               response_model=CategoryResponse,
               status_code=status.HTTP_200_OK)
async def deleted(category_id: int, db: AsyncSession = Depends(get_session)):
    obj = CategoryRepository(db, Category)
    result = await obj.delete(category_id)
    return result
