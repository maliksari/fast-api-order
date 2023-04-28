from fastapi import APIRouter, Depends
from starlette import status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.request.users import UserCreate, UserUpdate
from app.schemas.response.users import ResponseUser
from app.settings.database import get_session
from app.crud.user import UserRepository

router = APIRouter()


@router.get("/",
            tags=["Users"],
            summary="Kullanıcı listele....",
            response_description="Response ....",
            response_model=List[ResponseUser], status_code=status.HTTP_200_OK)
async def get_users(session: AsyncSession = Depends(get_session)):
    obj = UserRepository(session)
    users = await obj.get_users()
    return users


@router.post("/", tags=["Users"],
             summary="Yeni Kullanıcı oluştur",
             response_description="Response ....", response_model=ResponseUser, status_code=status.HTTP_201_CREATED)
async def register(user_data: UserCreate, db: AsyncSession = Depends(get_session)):
    obj = UserRepository(db)
    users = await obj.create_user(user_data)
    return users


@router.patch("/{user_id}", tags=["Users"],
              summary="Güncelle",
              response_description="Response ....", response_model=UserUpdate, status_code=status.HTTP_200_OK)
async def update_user(user_id: int, user_data: UserUpdate, db: AsyncSession = Depends(get_session)):
    obj = UserRepository(db)
    user = await obj.update_user(user_id, user_data)
    return user


@router.delete("/{user_id}", tags=["Users"],
               summary="Delete user",
               response_description="Response ....")
async def delete_a_user(user_id: int, db: AsyncSession = Depends(get_session)):
    obj = UserRepository(db)
    user = await obj.delete_user(user_id)
    return user


@router.get("/{user_id}", tags=["Users"],
            summary="Detail User",
            response_description="Response ....", response_model=ResponseUser, status_code=status.HTTP_200_OK)
async def get_user_by_id(user_id: int, db: AsyncSession = Depends(get_session)):
    obj = UserRepository(db)
    user = await obj.get_user_by_id(user_id)
    return user
