# -*- coding: utf-8 -*-
from models.MenuCard import MenuCard, item_exists

import logging
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi import APIRouter, status, HTTPException

# FastAPI app router
router = APIRouter(prefix="/kitchen/menu")


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


class MenuItem(BaseModel):
    """Model to represent a new item to be added to the menu"""
    name: str
    quantity: int
    price: int
    type: str


@router.get('/')
def get_menu():
    """
    Retrieve the menu items.

    This function serves the purpose of fetching the menu items, providing a snapshot of the available items on the menu
    card. It does not require any input parameters as it simply returns the menu without any specific filtering.

    Returns:
    - MenuCard: An instance of the MenuCard class containing information about the available menu items.

    Raises:
    - No specific exceptions are raised by this function.

    Example Usage:
    ```python
    menu = get_menu()
    print(menu.get_items())  # Output: {'item1': ..., 'item2': ..., ...}
    ```

    Notes:
    - The MenuCard class is expected to be properly initialized and available in the current scope.
    - This function is suitable for situations where a comprehensive view of the menu is needed without specific filtering.
    """
    log.info("Returning the menu card")
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=MenuCard.get_all_items(MenuCard)
    )


@router.post('/add')
def add_item(item: MenuItem):
    """
    Add a new item to the menu.

    This endpoint allows the addition of a new item to the menu by providing information about the item,
    including its name, quantity, price, and type. It checks if the item already exists in the menu
    before attempting to add it.

    Parameters:
    - item (MenuItem): The data representing the new item to be added.

    Returns:
    - JSONResponse: An HTTP response indicating the status of the operation.

    Raises:
    - HTTPException (status_code=409): If the item already exists in the menu.

    Example Usage:
    ```python
    # Request
    curl -X 'POST' \
      'http://127.0.0.1:8000/menu/add' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
      "item_name": "New Item",
      "item_quantity": 10,
      "item_price": 15.99,
      "item_type": "Main Course"
    }'

    # Response
    {
        "message": "Item added to the menu",
        "item": "New Item"
    }
    ```

    Notes:
    - The MenuItem model is expected to have attributes such as item_name, item_quantity, item_price, and item_type.
    - The MenuCard class should have a method add_item to insert the new item into the menu database table.
    - The endpoint returns a 201 Created status upon successful addition of the item.
    """
    if item_exists(item.name):  # Check if  item already exists in the menu
        log.error(f"Item already exists: {item.name}")
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Item already exists"
        )
    else:  # If the item does not exist, add it to the menu card database table
        new_item = MenuCard(
            item.name,
            item.quantity,
            item.price,
            item.type
        )
        MenuCard.add_item(new_item)
        log.info(f"Added a new item to the menu: {item.name}")
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "message": "Item added to the menu",
                "item": item.name
            }
        )
