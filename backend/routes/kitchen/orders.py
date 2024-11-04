from __future__ import annotations

import logging

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from models.Orders import get_all_orders

# FastAPI app router
router = APIRouter(prefix="/kitchen")


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


@router.get("/orders")
def get_orders(user_id: int = None):
    orders = get_all_orders(user_id)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=orders
    )
