#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from .config import settings

database_url = settings.DATABASE_CONNECTION

engine = create_async_engine(database_url, echo=True, future=True)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all())


async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with engine.connect() as conn:
        async with async_session(bind=conn) as session:
            yield session
