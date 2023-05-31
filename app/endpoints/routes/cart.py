from typing import Any, List, Optional
from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import Field, Session, SQLModel, create_engine, select, desc

from app.endpoints.auths.auth_handler import get_token_data
from app.settings.database import get_session
from app.models import Cart, CartItem, Product
from app.schemas.request.cart import CartRequest


router = APIRouter()


@router.post("", tags=["Cart"],
             summary="add to cart",
             response_description="..",
             response_model="",
             status_code=status.HTTP_201_CREATED)
async def add_to_cart(req: List[CartRequest], db: AsyncSession = Depends(get_session), token_data: Any = Depends(get_token_data)):
    user_id = token_data["user_id"]
    query = select(Cart).where(Cart.user_id == user_id).where(
        Cart.is_completed == False).where(Cart.is_active == True).order_by(desc(Cart.created_at))

    cart = await db.execute(query)
    cart = cart.fetchone()

    cart_id = cart[0].id
    # print("*****", cart_id)

    if cart is None:
        cart = Cart(user_id=user_id, is_active=True,
                    is_completed=False, created_by=user_id)
        db.add(cart)
        await db.commit()
        await db.refresh(cart)
        cart_id = cart.id
        # print("*-*-*-*-*-*-", cart.id)
    total_price=0
    for i in req:
        product_query = select(Product).where(Product.id == i.product_id)
        product = await db.execute(product_query)
        product = product.fetchone()[0]
        product_id = product.id
        stock_amount = product.stock_amount
        item_price = product.price * i.quantity
        total_price += item_price
        print("******", product_id,"***",stock_amount,"***",item_price,"**",total_price)
        """
        Not:
         - Cart item ekle stok miktarını güncelle
         - Cart total price güncelle 
         - response model yaz 

        """

    return {"test": ""}
