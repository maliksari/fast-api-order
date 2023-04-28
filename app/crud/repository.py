from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from starlette import status
from datetime import datetime
from starlette.responses import JSONResponse


class BaseRepository:
    def __init__(self, db: AsyncSession, model):
        self.db = db
        self.model = model

    async def create(self, instance, created_by_id):
        instance_dict = instance.dict(exclude_unset=True)
        instance_dict.update({
            "created_by": created_by_id,
        })

        result = self.model(**instance_dict)
        self.db.add(result)
        try:
            await self.db.commit()
            await self.db.refresh(result)
            return result
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Created failed ",
            )

    async def get_all(self):
        query = await self.db.execute(select(self.model))
        result = query.scalars().all()
        return result

    async def get_by_id(self, id):
        result = await self.db.get(self.model, id)
        return result

    async def update(self, instance, id, modified_by_id):
        obj = await self.db.get(self.model, id)
        if not obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"{self.model.__name__} not found with id: {id}")
        instance_dict = instance.dict(exclude_unset=True)
        instance_dict.update({
            "modified_at": datetime.now(),
            "modified_by": modified_by_id
        })
        for key, value in instance_dict.items():
            setattr(obj, key, value)
        try:
            self.db.add(obj)
            await self.db.commit()
            await self.db.refresh(obj)
        except Exception as e:
            raise HTTPException(
                detail=f"Kayıt güncellenmedi: {e}", status_code=status.HTTP_400_BAD_REQUEST)
        return obj

    async def delete(self, id):
        obj = await self.db.get(self.model, id)
        if not obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"{self.model.__name__} not found with id: {id}")
        try:
            await self.db.delete(obj)
            await self.db.commit()
        except Exception as e:
            raise HTTPException(
                detail=f"Kayıt Silinemedi: {e}", status_code=status.HTTP_400_BAD_REQUEST)
        return JSONResponse({
            "status": "Success",
            "message": "Kayıt silindi.."
        }, status_code=status.HTTP_200_OK)
