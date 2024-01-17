from fastapi import APIRouter, Depends, HTTPException, Header
from backend.controller.token import verify_access_token

router = APIRouter(
    prefix="/user/api",
)


# Dependency to check for a valid JWT token in the header
def check_jwt_token(authorization: str = Header(..., description="JWT token")):
    token_prefix, token = authorization.split()
    if token_prefix.lower() != "bearer":
        raise HTTPException(
            status_code=401,
            detail="Invalid token type. Use Bearer authentication.",
        )
    return verify_access_token(token)


@router.get('/', dependencies=[Depends(check_jwt_token)])
def check_connection():
    """To check connection"""
    print("Checking successful")
    return "Checking successful"


@router.get('/menu', dependencies=[Depends(check_jwt_token)])
def menu():
    """To check connection"""
    print("Checking successful")
    return {"message": "Menu"}
