"""File which manages the items to be displayed"""
from PyQt5 import QtCore, QtWidgets
from pydantic import BaseModel
import httpx as api

BASE_URL = "http://127.0.0.1:5000"

ROUTE = "/kitchen/menu/"


class MenuItem:
    """Model to represent a new item to be added to the menu"""
    name: str = None
    quantity: int = None
    price: int = None
    type: str = None

    def __repr__(self) -> str:
        return f"<MenuItem(name={self.name}, price={self.price})>"


def menu_item(
        parent_widget: QtWidgets,
        item_name: str,
        item_price: int = 0,
        available: bool = True
):
    """Function to add an item to the Main Window"""

    # Initialising a menu item
    menu_item = QtWidgets.QGroupBox(parent_widget)
    menu_item.setObjectName("menu_item")
    menu_item.setMinimumSize(QtCore.QSize(111, 0))
    menu_item.setFlat(False)
    menu_item.setCheckable(True)
    menu_item.setChecked(available)

    # Initialising the layout of a menu item
    menu_item_layout = QtWidgets.QHBoxLayout(menu_item)
    menu_item_layout.setObjectName("menu_item_layout")

    # Initialising the left spacer
    left_spacer = QtWidgets.QSpacerItem(
        40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
    )
    # Add the left spacer to the menu item
    menu_item_layout.addItem(left_spacer)

    # Initialising the price label
    price_label = QtWidgets.QLabel(menu_item)
    price_label.setObjectName("price_label")
    price_label.setAlignment(
        QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
    )
    # Add the price label to the menu item
    menu_item_layout.addWidget(price_label)

    # Initialising the price spinbox
    price = QtWidgets.QSpinBox(menu_item)
    price.setObjectName("price")
    price.setValue(item_price)
    _size = QtWidgets.QSizePolicy(
        QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
    )
    _size.setHorizontalStretch(0)
    _size.setVerticalStretch(0)
    _size.setHeightForWidth(price.sizePolicy().hasHeightForWidth())
    price.setSizePolicy(_size)
    price.setMaximum(999)
    # Add the price spinbox to the menu item layout
    menu_item_layout.addWidget(price)

    # Initialising the spacer between the price and quantity
    middle_spacer = QtWidgets.QSpacerItem(
        40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
    )
    # Add the middle spacer to the menu item layout
    menu_item_layout.addItem(middle_spacer)

    # Initialising the quantity label
    quantity_label = QtWidgets.QLabel(menu_item)
    quantity_label.setObjectName("quantity_label")
    quantity_label.setAlignment(
        QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
    )
    # add the quantity label to the menu item layout
    menu_item_layout.addWidget(quantity_label)

    # Initialising the quantity spinbox
    quantity = QtWidgets.QSpinBox(menu_item)
    _size = QtWidgets.QSizePolicy(
        QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
    )
    _size.setHorizontalStretch(0)
    _size.setVerticalStretch(0)
    _size.setHeightForWidth(quantity.sizePolicy().hasHeightForWidth())
    quantity.setSizePolicy(_size)
    quantity.setObjectName("quantity")
    quantity.setMaximum(999)
    # Add the quantity spinbox to the menu item layout
    menu_item_layout.addWidget(quantity)

    # Initialising the right spacer to the menu item
    right_spacer = QtWidgets.QSpacerItem(
        40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
    )
    # Add the right spacer to the menu item layout
    menu_item_layout.addSpacerItem(right_spacer)

    # Re translate UI
    _translate = QtCore.QCoreApplication.translate
    menu_item.setTitle(_translate("main_window", f"{item_name}"))
    price_label.setText(_translate("main_window", "Price:"))
    price.setPrefix(_translate("main_window", "₹ "))
    quantity_label.setText(_translate("main_window", "Quantity:"))
    quantity.setSuffix(_translate("main_window", " serves"))

    return menu_item


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
        print("Received item price is", item_to_add)
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
            menu_item.name = item["item_name"]
            menu_item.price = item["item_price"]
            menu_item.quantity = item["item_quantity"]
            menu_item.type = item["item_type"]

            item_key = menu_item.name.lower().replace(" ", "")

            self.item_filters[menu_item.type][item_key] = menu_item
            self.item_filters["All Items"][item_key] = menu_item

