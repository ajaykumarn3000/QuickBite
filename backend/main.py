# -*- coding: utf-8 -*-
from fastapi import FastAPI, APIRouter, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from routes.user.api import router as user_api_router
from routes.user.auth import router as user_auth_router
from routes.kitchen.menu_card import router as menu_card_router

app = FastAPI()

version = "v1"

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(f"/{version}")
def root():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content="Connected to QuickBite CMS Backend",
    )


# Create a global API router with the /{version} prefix
api_router = APIRouter(prefix=f"/{version}")

# Include all individual routers under this main API router
api_router.include_router(user_auth_router)
api_router.include_router(user_api_router)
api_router.include_router(menu_card_router)

# Include the API router in the FastAPI app
app.include_router(api_router)
