#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Optional
from pydantic import (BaseSettings, Field)

from app.settings.local_conf import DATABASE_URL, HASH_CODE


class Settings(BaseSettings):
    DATABASE_CONNECTION: Optional[str] = Field(
        DATABASE_URL, env='DATABASE_CONNECTION_STR')
    HASH_CODE: Optional[str] = Field(
        HASH_CODE, env='HASH_CODE')
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 *8  # 60 minutes * 24 hours * 1 days = 1 days
    PROJECT_NAME: str = "Fast API Order"
    PROJECT_DESCRIPTION: str = "Proje bilgileri"
    PROJECT_VERSION: str = "0.0.1"

    class Config:
        case_sensitive = True


settings = Settings()
