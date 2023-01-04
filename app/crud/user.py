from sqlmodel import  select
from fastapi import  HTTPException, status
from datetime import datetime
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from app.schemas.request.users import UserUpdate
from app.models.users import User
# from app.crud.repository import Repository
from app.endpoints.auths.auth_handler import get_password_hash


class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_user_by_id(self, user_id: int) -> Optional[User]:
        user = await self.db.get(User, user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User not found with id: {user_id}",
            )

        return user

    async def get_users(self) -> List[User]:
        result = await self.db.execute(select(User))
        users = result.scalars().all()
        return users

    async def create_user(self, user: User) -> User:
        result = await self.db.execute(select(User))
        users = result.scalars().all()

        if any(x.username == user.username for x in users):
            raise HTTPException(
                status_code=400, detail=f'{user.username} kullanıcı adı zaten kayıtlı')

        hashed_pwd = get_password_hash(user.password)
        user = {
            "username": user.username,
            "name": user.name,
            "surname": user.surname,
            "age": user.age,
            "password": hashed_pwd,
        }

        try:
            user_create = User(**user)
            self.db.add(user_create)
            await self.db.commit()
            await self.db.refresh(user_create)

        except Exception as e:
            return JSONResponse({
                "status": "Failed",
                "message": "Kayıt oluşturalamadı: {}".format(str(e))
            }, status_code=status.HTTP_400_BAD_REQUEST)
        return user_create

    async def update_user(self, user_id: int, user_data: UserUpdate) -> User:
        user = await self.db.get(User, user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User not found with id: {user_id}",
            )

        user_dict = user_data.dict(exclude_unset=True)
        user_dict.update({
            "modified_at": datetime.now()
        })

        for key, value in user_dict.items():
            setattr(user, key, value)
        try:
            self.db.add(user)
            await self.db.commit()
            await self.db.refresh(user)
        except Exception as e:
            return JSONResponse({
                "status": "Failed",
                "message": "Kayıt güncellenmedi: {}".format(str(e))
            }, status_code=status.HTTP_400_BAD_REQUEST)
        return user

    async def delete_user(self, user_id) -> User:
        user = await self.db.get(User, user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User not found with id: {user_id}",
            )
        try:
            await self.db.delete(user)
            await self.db.commit()
        except Exception as e:
            return JSONResponse({
                "status": "Failed",
                "message": "Kayıt silinemedi: {}".format(str(e))
            }, status_code=status.HTTP_400_BAD_REQUEST)

        return JSONResponse({
            "status": "Success",
            "message": "Kayıt silindi.."
        }, status_code=status.HTTP_200_OK)
