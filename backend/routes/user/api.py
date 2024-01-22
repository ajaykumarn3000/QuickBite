import logging

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
def check_connection(decoded_token: dict = Depends(check_jwt_token)):
    print(decoded_token)
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
    """
    This endpoint retrieves the user's cart.

    It uses the HTTP GET method and is located at the path '/cart'.

    This function is dependent on the check_jwt_token function, which verifies the JWT token in the request header.

    Parameters:
    user_data (dict): User data obtained from the JWT token. It is expected to contain the user's ID.

    Returns:
    JSONResponse: A JSON response indicating the status of the operation. If successful, it returns a status code of 200 and the content of the user's cart.
    If an error occurs, it returns a status code of 400 and a message detailing the error.

    Raises:
    HTTPException: If an error occurs during the operation, an HTTPException is raised with a status code of 400 and a detail message containing the error.
    """
    user_id = user_data['uid']
    log.info(f"User: {user_id} requested to view their cart")
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=Cart(user_id).get_cart()
    )


@router.post('/cart/add/{item}', dependencies=[Depends(check_jwt_token)])
def add_item(item: int, user_data=Depends(check_jwt_token)):
    """
    This endpoint adds an item to the user's cart.

    It uses the HTTP POST method and is located at the path '/cart/add/{item}'.
    The item parameter in the path is an integer representing the ID of the item to be added.

    This function is dependent on the check_jwt_token function, which verifies the JWT token in the request header.

    Parameters:
    item (int): The ID of the item to be added to the cart.
    user_data (dict): User data obtained from the JWT token. It is expected to contain the user's ID.

    Returns:
    JSONResponse: A JSON response indicating the status of the operation. If successful, it returns a status code of 200 and a message indicating the item has been added and the available quantity of the item.
    If an error occurs, it returns a status code of 400 and a message detailing the error.

    Raises:
    HTTPException: If an error occurs during the operation, an HTTPException is raised with a status code of 400 and a detail message containing the error.
    """
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
    """
    This endpoint removes an item from the user's cart.

    It uses the HTTP POST method and is located at the path '/cart/remove/{item}'.
    The item parameter in the path is an integer representing the ID of the item to be removed.

    This function is dependent on the check_jwt_token function, which verifies the JWT token in the request header.

    Parameters:
    item (int): The ID of the item to be removed from the cart.
    user_data (dict): User data obtained from the JWT token. It is expected to contain the user's ID.

    Returns:
    JSONResponse: A JSON response indicating the status of the operation. If successful, it returns a status code of 200 and a message indicating the item has been removed and the available quantity of the item.
    If an error occurs, it returns a status code of 400 and a message detailing the error.

    Raises:
    HTTPException: If an error occurs during the operation, an HTTPException is raised with a status code of 400 and a detail message containing the error.
    """
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
    """
    This endpoint deletes an item from the user's cart.

    It uses the HTTP DELETE method and is located at the path '/cart/delete/{item}'.
    The item parameter in the path is an integer representing the ID of the item to be deleted.

    This function is dependent on the check_jwt_token function, which verifies the JWT token in the request header.

    Parameters:
    item (int): The ID of the item to be deleted from the cart.
    user_data (dict): User data obtained from the JWT token. It is expected to contain the user's ID.

    Returns:
    JSONResponse: A JSON response indicating the status of the operation. If successful, it returns a status code of 200 and a message indicating the item has been deleted.
    If an error occurs, it returns a status code of 400 and a message detailing the error.

    Raises:
    HTTPException: If an error occurs during the operation, an HTTPException is raised with a status code of 400 and a detail message containing the error.
    """
    user_id = user_data['uid']
    log.info(f"User: {user_id} has requested to delete item: {item} from their cart")
    try:
        Cart(user_id).delete_item(item)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"message": "Deleted item from cart"}
        )
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
