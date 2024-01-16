from routes.user.auth import router as user_auth_router
from routes.user.api import router as user_api_router
from routes.staff.auth import router as staff_auth_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=user_auth_router)
app.include_router(router=staff_auth_router)
app.include_router(router=user_api_router)
