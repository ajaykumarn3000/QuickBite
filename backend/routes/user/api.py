import logging
import models.Users
import models.MenuCard

from fastapi import APIRouter, Depends, HTTPException, Header, status, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from controller.token import verify_access_token
from models.Cart import Cart

router = APIRouter(
    prefix="/user/api",
)


def logger_object():
    """Function to create a logger object to log the backend to the console"""
    logger = logging.getLogger(__name__)

    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger


log = logger_object()


class CartItem(BaseModel):
    item_id: int


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


@router.get('/cart', dependencies=[Depends(check_jwt_token)])
def get_cart(user_data=Depends(check_jwt_token)):
    user_id = user_data['uid']
    log.info(f"User: {user_id} requested to view their cart")
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=Cart(user_id).get_cart()
    )


@router.post('/cart/add/{item}', dependencies=[Depends(check_jwt_token)])
def add_item(item: int, user_data=Depends(check_jwt_token)):
    user_id = user_data['uid']
    log.info(f"User: {user_id} has requested to add item: {item} to their cart")
    try:
        Cart(user_id).add_item(item)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": "Added item to cart",
                "available quantity": Cart(user_id).item_exists(item).quantity
            }
        )
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.post('/cart/remove/{item}', dependencies=[Depends(check_jwt_token)])
def remove_item(item: int, user_data=Depends(check_jwt_token)):
    user_id = user_data['uid']
    log.info(f"User: {user_id} has requested to remove item: {item} from their cart")
    try:
        Cart(user_id).remove_item(item)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": "Removed item from cart",
                "available quantity": Cart(user_id).item_exists(item).quantity
            }
        )
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.delete('/cart/delete/{item}', dependencies=[Depends(check_jwt_token)])
def delete_item(item: int, user_data=Depends(check_jwt_token)):
    user_id = user_data['uid']
    log.info(f"User: {user_id} has requested to delete item: {item} from their cart")
    try:
        Cart(user_id).delete_item(item)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": "Deleted item from cart",
            }
        )
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
