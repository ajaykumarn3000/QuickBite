"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from src.components.Auth.Auth import Auth


class State(rx.State):
    token: str = ""

    def set_token(self, token: str):
        self.token = token

    def is_authenticated(self):
        return False


@rx.page(route="/auth", title="login to QuickBite")
def auth() -> rx.Component:
    return Auth()


# Create app instance and add index page.
app = rx.App(stylesheets=["Auth.css"])
