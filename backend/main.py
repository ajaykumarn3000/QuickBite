from routes.user.auth import router as user_auth_router
from fastapi import FastAPI, Request

# FastAPI app
app = FastAPI()
app.include_router(router=user_auth_router)
