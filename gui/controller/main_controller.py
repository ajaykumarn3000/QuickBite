"""File which manages the items to be displayed"""
from PyQt5 import QtCore, QtWidgets
from pydantic import BaseModel
import httpx as api

BASE_URL = "http://127.0.0.1:5000"

ROUTE = "/kitchen/menu/"


class MenuItem:
    """Model to represent a new item to be added to the menu"""
    id: int = None
    name: str = None
    quantity: int = None
    price: int = None
    type: str = None

    def __repr__(self) -> str:
        return f"<MenuItem(id={self.id}, name={self.name}, price={self.price})>"


class ItemView:
    """Class which contains the items to display in the Menu Item View"""
    item_filters = {
        "All Items": dict(),
        "Breakfast": dict(),
        "Lunch": dict(),
        "Snacks": dict(),
        "Drinks": dict(),
        "Beverages": dict(),
        "Ice Cream": dict()
    }

    def add_menu_item(self, item_to_add: dict) -> None:
        item = MenuItem()
        item.name = item_to_add["name"]
        item.quantity = item_to_add["quantity"]
        item.price = item_to_add["price"]
        item.type = item_to_add["type"]

        item_key = item.name.lower().replace(" ", "")

        self.item_filters[item.type][item_key] = item
        self.item_filters["All Items"][item_key] = item

    def sync(self):
        response = api.get(url=BASE_URL + ROUTE).json()
        for item in response:
            menu_item = MenuItem()
            menu_item.id = item["item_id"]
            menu_item.name = item["item_name"]
            menu_item.price = item["item_price"]
            menu_item.quantity = item["item_quantity"]
            menu_item.type = item["item_type"]

            item_key = menu_item.name.lower().replace(" ", "")

            self.item_filters[menu_item.type][item_key] = menu_item
            self.item_filters["All Items"][item_key] = menu_item
