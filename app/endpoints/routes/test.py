from typing import Any
from fastapi import APIRouter, Depends
from starlette import status

from app.endpoints.auths.auth_handler import get_token_data

router = APIRouter()


@router.get("/",
            tags=["Test"],
            summary="test",
            response_description="Response ....",
            status_code=status.HTTP_200_OK)
async def get_users(token_data: Any = Depends(get_token_data)):
    return token_data
