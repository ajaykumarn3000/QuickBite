"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from src.components.Auth.Auth import Auth
from src.components.Navbar.Navbar import Navbar
from src.components.Menu.menu import Menu
from src.components.Cart.cart import Cart

# state
from src.state import AuthState

# @rx.page(route="/auth", title="login to QuickBite")
# def auth() -> rx.Component:
#     return Auth()


@rx.page(route="/", title="QuickBite")
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

    # return rx.box(
    #     rx.cond(TestState.test, rx.text("Hello"), rx.text("World")),
    #     rx.button("Toggle", on_click=TestState.toggle_test)
    # )


# Create app instance and add index page.
app = rx.App(stylesheets=["Auth.css", "Cart.css", "index.css"])
