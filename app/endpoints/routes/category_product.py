from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.models.category import Category
from app.models.product import Product, CategoryProduct
from app.crud.category import CategoryRepository
from app.schemas.response.product import ProductResponse
from app.schemas.response.category_product import CategoryProductsResponse
from app.settings.database import get_session

router = APIRouter()


@router.get("/{category_id}/products", tags=["Category-Products"],
            summary="get category product",
            response_description="Response ....",
            response_model=CategoryProductsResponse,
            status_code=status.HTTP_200_OK)
async def get_category_products(category_id: int, db: AsyncSession = Depends(get_session)):

    obj = CategoryRepository(db, Category)
    category = await obj.get_by_id(category_id)

    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category not found with id: {category_id}")

    products = await db.execute(select(Product).join(CategoryProduct).where(CategoryProduct.category_id == category_id))

    prods = products.scalars().all()
    product_responses = [ProductResponse.from_orm(
        product) for product in prods]
    category_products_response = CategoryProductsResponse(
        name=category.name,
        category_code=category.category_code,
        list_order=category.list_order,
        products=product_responses
    )
    return category_products_response
