# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


def add_menu_item(parent_widget, item_name: str, item_price: int = 0, available: bool = True):
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

    # Retranslate UI
    _translate = QtCore.QCoreApplication.translate
    menu_item.setTitle(_translate("main_window", f"{item_name}"))
    price_label.setText(_translate("main_window", "Price:"))
    price.setPrefix(_translate("main_window", "₹ "))
    quantity_label.setText(_translate("main_window", "Quantity:"))
    quantity.setSuffix(_translate("main_window", " serves"))

    return menu_item


class MainWindow:
    """Class to create the main window of the admin"""

    def __init__(self):
        """Constructor of the class"""

        # Initialising the central widget
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")

        # Initialising the layout of the main window
        self.window_layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.window_layout.setObjectName("window_layout")

        # Initialising the toolbar of the main window
        self.toolbar = QtWidgets.QHBoxLayout()
        self.toolbar.setObjectName("toolbar")

        # Initialising the button to add a new item
        self.add_button = QtWidgets.QToolButton(self.central_widget)
        self.add_button.setObjectName("add_button")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("../assets/icons/add_button.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.add_button.setIcon(icon)
        self.add_button.clicked.connect(self.on_click)
        # Add the add button to the toolbar
        self.toolbar.addWidget(self.add_button)

        # Initialising the spacer which pushes the add button to the right
        toolbar_spacer = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        # Add the toolbar spacer to the toolbar
        self.toolbar.addItem(toolbar_spacer)

        # Add the toolbar to the window layout
        self.window_layout.addLayout(self.toolbar)

        # Initialising the scroll area
        self.scroll_area = QtWidgets.QScrollArea(self.central_widget)
        self.scroll_area.setObjectName("scroll_area")
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
        )

        # Initialising the scroll area widget contents
        self.scroll_area_widget_contents = QtWidgets.QWidget()
        self.scroll_area_widget_contents.setObjectName("scroll_area_widget_contents")
        self.scroll_area_widget_contents.setGeometry(QtCore.QRect(0, 0, 479, 458))

        # Initialising the scroll area layout inside of the scroll area
        self.scroll_area_layout = QtWidgets.QVBoxLayout(self.scroll_area_widget_contents)
        self.scroll_area_layout.setObjectName("scroll_area_layout")
        item = add_menu_item(self.scroll_area_widget_contents, 'Chips')

        self.scroll_area_layout.addWidget(item)

        # Add the menu item to the window layout
        # self.scroll_area_layout.removeWidget(item)

        # Initialising the vertical spacer that pushes item to the top of scroll
        self.vertical_spacer = QtWidgets.QSpacerItem(
            17, 302, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )

        # Add the vertical spacer to the scroll area layout
        self.scroll_area_layout.addItem(self.vertical_spacer)

        # Add the scroll area widget contents to the scroll area
        self.scroll_area.setWidget(self.scroll_area_widget_contents)

        # Add the scroll area to the window layout
        self.window_layout.addWidget(self.scroll_area)

        # Initialising the status bar of the main window
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")

    def on_click(self):
        children = self.scroll_area_layout.count()
        menu_item = add_menu_item(self.scroll_area_widget_contents, 'Chips')
        self.scroll_area_layout.insertWidget(children - 1, menu_item)
        print("Before removal")
        self.scroll_area_layout.removeWidget(menu_item)
        print("After removal")

    def setup_ui(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(505, 549)
        main_window.setMinimumSize(QtCore.QSize(359, 0))
        main_window.setCentralWidget(self.central_widget)
        main_window.setStatusBar(self.statusbar)
        self.retranslate_ui(main_window)

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "MainWindow"))
        self.add_button.setStatusTip(_translate("main_window", "Click to add an item"))
        self.add_button.setText(_translate("main_window", "..."))
        self.add_button.setShortcut(_translate("main_window", "Ctrl+N"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setup_ui(main_window)
    main_window.show()
    sys.exit(app.exec_())
