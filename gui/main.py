import sys
import httpx as api
from PyQt5 import QtWidgets, QtCore
from views.main_window import Ui_main_window
from views.add_dialog import Ui_add_dialog
from controller.database_controller import orders_model
from controller.main_controller import BASE_URL, ROUTE, MenuItem, ItemView
from assets import app_icons


def edit_item_quantity(item_id: int, item_quantity: int):
    response = api.post(
        f"{BASE_URL}{ROUTE}edit/{item_id}",
        params={"item_quantity": item_quantity}
    )


def edit_item_price(item_id: int, item_price: int):
    response = api.post(
        f"{BASE_URL}{ROUTE}edit/{item_id}",
        params={"item_price": item_price}
    )


def menu_item(
    parent_widget: QtWidgets,
    item_id: int,
    item_name: str,
    item_price: int = 0,
    item_quantity: int = 0,
    item_availability: bool = True
):
    """Function to add an item to the Main Window"""

    # Initialising a menu item
    menu_item = QtWidgets.QGroupBox(parent_widget)
    menu_item.setObjectName("menu_item")
    menu_item.setMinimumSize(QtCore.QSize(111, 0))
    menu_item.setFlat(False)
    menu_item.setCheckable(True)
    menu_item.setChecked(item_availability)

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
    # Update the value in the backend whenever the quantity is changed
    price.valueChanged.connect(
        lambda: edit_item_price(
            item_id=item_id,
            item_price=price.value()
        )
    )

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
    quantity.setValue(item_quantity)
    quantity.setMaximum(999)
    # Add the quantity spinbox to the menu item layout
    menu_item_layout.addWidget(quantity)
    # Update the value in the backend whenever the quantity is changed
    quantity.valueChanged.connect(
        lambda: edit_item_quantity(
            item_id=item_id,
            item_quantity=quantity.value()
        )
    )

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


class AddDialog(QtWidgets.QDialog, Ui_add_dialog):
    def __init__(self, *args, **kwargs):
        super(AddDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.button_box.accepted.connect(self.on_accepting)
        self.show()

    def on_accepting(self):
        quantity = int(self.quantity.text()
            .replace(self.quantity.prefix(), "")
            .replace(self.quantity.suffix(), "")
        )
        price = int(self.price.text()
            .replace(self.price.prefix(), "")
            .replace(self.price.suffix(), "")
        )
        item_to_add: dict = {
            "name": self.name.text(),
            "quantity": quantity,
            "price": price,
            "type": self.type.currentText()
        }
        response = api.post(BASE_URL + ROUTE + "add", json=item_to_add)
        if response.status_code == 201:
            print(f"Item: {item_to_add} has been added to the database")
            ItemView().add_menu_item(item_to_add)
            self.accept()
        else:
            print("Some error has occurred...")
            print(response.json())


class MainWindow(QtWidgets.QMainWindow, Ui_main_window):
    display_items: list = []

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.add_dialog = None
        self.setupUi(self)
        self.show()
        self.setWindowTitle("QuickBite Admin App")
        self.display_orders.setModel(orders_model)
        self.fetch_orders.triggered.connect(lambda: orders_model.select())
        self.refresh.triggered.connect(self.sync_with_db)
        self.filter_items.currentTextChanged.connect(self.refresh_items)
        self.add_action.triggered.connect(self.launch_add_dialog)
        self.searchbar.textEdited.connect(self.refresh_items)

    def refresh_items(self):
        text = self.searchbar.text()
        text = text.lower().replace(" ", "") if len(text) >= 2 else ""
        items = ItemView().item_filters[self.filter_items.currentText()]
        filtered_items = [items[key] for key in filter(lambda item: item.__contains__(text), items)]

        for index in range(self.verticalLayout_2.count() - 2, -1, -1):
            item = self.verticalLayout_2.itemAt(index).widget()
            self.verticalLayout.removeWidget(item)
            item.setParent(None)
            del item

        # TODO: Optimize by only refreshing when the filtered_items have changed

        for item in filtered_items:
            item = menu_item(parent_widget=self.scroll_area_widget_contents,
                             item_id=item.id,
                             item_name=item.name,
                             item_price=item.price,
                             item_quantity=item.quantity,
                             item_availability=True
                             )
            self.verticalLayout_2.insertWidget(0, item)

    def launch_add_dialog(self):
        self.add_dialog = AddDialog()
        # Sync is happening before accepting AddDialog
        self.sync_with_db()

    def sync_with_db(self):

        for index in range(self.verticalLayout_2.count() - 2, -1, -1):
            item = self.verticalLayout_2.itemAt(index).widget()
            self.verticalLayout.removeWidget(item)
            item.setParent(None)
            del item

        ItemView().sync()

        for index, item in enumerate(ItemView.item_filters[self.filter_items.currentText()].values()):
            item = menu_item(parent_widget=self.scroll_area_widget_contents,
                item_id=item.id,
                item_name=item.name,
                item_price=item.price,
                item_quantity=item.quantity,
                item_availability=True
            )
            self.verticalLayout_2.insertWidget(index, item)

        # Reset the searchbar
        self.searchbar.setText("")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())
