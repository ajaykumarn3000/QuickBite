"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx

from src.components.Auth.Auth import Auth


def index() -> rx.Component:
    return Auth()


# Create app instance and add index page.
app = rx.App(stylesheets=["Auth.css"])
app.add_page(index)
