#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uvicorn


from fastapi import FastAPI, APIRouter, Depends
from fastapi.middleware.cors import CORSMiddleware

from app.settings.config import settings
from app.settings.docs import tags_metadata, contact, terms_of_service, license_info, description
from app.endpoints.auths.auth_jwt import JWTBearer

from app.endpoints.routes.users import router as users_router
from app.endpoints.routes.token import router as token_router
from app.endpoints.routes.test import router as test_router
from app.endpoints.routes.category import router as category_router
from app.endpoints.routes.product import router as product_router


origins = [
    "https://localhost",
    "https://localhost:8080",
]

app = FastAPI(openapi_tags=tags_metadata,
              title=settings.PROJECT_NAME,
              description=description,
              version=settings.PROJECT_VERSION,
              terms_of_service=terms_of_service,
              contact=contact,
              license_info=license_info,
              docs_url="/docs", redoc_url=None,
              openapi_url="/openapi.json")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


router = APIRouter()
# Yeni routerları ekle
router.include_router(users_router, prefix='/users',
                      tags=["Users"], dependencies=[Depends(JWTBearer())])


router.include_router(category_router, prefix="/category",
                      tags=['Category'], dependencies=[Depends(JWTBearer())])

router.include_router(product_router, prefix='/product',
                      tags=["Product"], dependencies=[Depends(JWTBearer())])
router.include_router(test_router, prefix='/test',
                      tags=["Test"], dependencies=[Depends(JWTBearer())])
router.include_router(token_router, prefix='/token', tags=["Token"])


# bütün routerlara dependencies ekle
# app.include_router(api_router,dependencies=[Depends(JWTBearer())])

app.include_router(router)

"""
Token ile çalışmak için ekle
dependencies=[Depends(JWTBearer())]
"""


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
