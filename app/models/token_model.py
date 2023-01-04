from typing import Optional
from pydantic import BaseModel


class TokenModel(BaseModel):
    user_id: Optional[int] = None
    exp: Optional[float] = ''
    iat: Optional[float] = ''

    class Config:
        title = "Token içindeki veri modeli"
