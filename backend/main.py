# -*- coding: utf-8 -*-
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.user.api import router as user_api_router
from routes.user.auth import router as user_auth_router
from routes.kitchen.menu_card import router as menu_card_router

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Connected to QuickBite API"}


app.include_router(router=user_auth_router)
app.include_router(router=user_api_router)
app.include_router(router=menu_card_router)
