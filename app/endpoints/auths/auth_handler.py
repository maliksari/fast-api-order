import jwt
import time

from typing import Dict
from fastapi import Request, HTTPException
from passlib.context import CryptContext
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.models.token_model import TokenModel
from app.settings.config import settings

expire_at = settings.ACCESS_TOKEN_EXPIRE_MINUTES

JWT_ALGORITHM = "HS256"
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def token_response(token: str):
    return {
        "access_token": token
    }


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(
            token, settings.HASH_CODE, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["exp"] >= time.time() else None
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Expired signature')
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail='Invalid token')


async def get_token_data(request: Request):
    auth = HTTPBearer()
    credentials: HTTPAuthorizationCredentials = await auth.__call__(request)
    token_object = decodeJWT(credentials.credentials)
    return token_object


def signJWT() -> Dict[str, str]:
    token_model = TokenModel(
        user_id=None,
        exp=time.time() + expire_at,
        iat=time.time(),
    )
    token = jwt.encode(token_model.__dict__,
                       settings.hash_code, algorithm=JWT_ALGORITHM)
    return token_response(token)


def createJWT(user_id: any) -> Dict[str, str]:
    token_model = TokenModel(
        user_id=user_id,
        exp=time.time() + expire_at,
        iat=time.time(),
    )
    token = jwt.encode(token_model.__dict__,
                       settings.HASH_CODE, algorithm=JWT_ALGORITHM)
    return token_response(token)


def get_password_hash(password: str):
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)
