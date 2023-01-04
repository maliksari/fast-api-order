from fastapi import APIRouter, HTTPException, Depends
from starlette import status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.schemas.request.login import LoginRequest
from app.settings.database import get_session
from app.endpoints.auths.auth_handler import verify_password, createJWT
from app.models import User

router = APIRouter()


@router.post("/login",
             tags=["Token"],
             summary="Access token",
             response_description="Response ....",
             status_code=status.HTTP_200_OK)
async def login(login: LoginRequest, session: AsyncSession = Depends(get_session)):
    user = select(User.id, User.password, User.username).where(
        User.username == login.username)
    user = await session.execute(user)
    user = user.first()

    if not user:
        raise HTTPException(
            status_code=401, detail='Invalid username and/or password')

    verified = verify_password(login.password, user.password)
    if not verified:
        raise HTTPException(
            status_code=401, detail='Invalid username and/or password')

    token = createJWT(user.id)
    return token
