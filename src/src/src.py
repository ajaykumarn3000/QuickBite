"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from src.components.Auth.Auth import Auth
from src.components.Navbar.Navbar import Navbar
from src.components.Menu.menu import Menu
from src.components.Cart.cart import Cart


class State(rx.State):
    token: str = ""

    def set_token(self, token: str):
        self.token = token

    def is_authenticated(self):
        return False


@rx.page(route="/auth", title="login to QuickBite")
def auth() -> rx.Component:
    return Auth()


@rx.page(route="/", title="QuickBite")
def index() -> rx.Component:
    return rx.fragment(Navbar(), 
    rx.box(Menu(), Cart(), class_name="flex grow overflow-y-auto relative sm:pb-2")
    )


# Create app instance and add index page.
app = rx.App(stylesheets=["Auth.css", "Cart.css", "index.css"])
