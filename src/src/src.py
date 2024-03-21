"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from src.components.Auth.Auth import Auth
from src.components.Navbar.Navbar import Navbar
from src.components.Menu.menu import Menu
from src.components.Cart.cart import Cart
from src.components.Orders.OrderPage import Orders
from src.components.Cart.success import Success

# state
from src.state import AuthState

# @rx.page(route="/auth", title="login to QuickBite")
# def auth() -> rx.Component:
#     return Auth()

@rx.page(route="/orders", title="QuickBite")
def orders() -> rx.Component:
    return rx.cond(
        AuthState.is_logged_in,
        rx.fragment(
            Navbar(AuthState),
            Orders(AuthState),
        ),
        Auth(AuthState),
    
    )

@rx.page(route="/", title="QuickBite", on_load=[AuthState.get_cart, AuthState.get_menu] )
def index() -> rx.Component:
    
    return rx.cond(
        AuthState.is_logged_in,
        rx.fragment(
            Navbar(AuthState),
            rx.chakra.box(
                Menu(),
                Cart(),
                class_name="flex grow overflow-y-auto relative sm:pb-2",
            ),
        ),
        Auth(AuthState),
    )

@rx.page(route="/success", title="QuickBite")
def success() -> rx.Component:
    return Success()


# Create app instance and add index page.
app = rx.App(stylesheets=["Auth.css", "Cart.css", "index.css"])
