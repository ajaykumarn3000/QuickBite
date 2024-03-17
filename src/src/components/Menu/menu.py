import reflex as rx
from src.components.Menu.menu_item import MenuItem
import time

from src.state import AuthState

# class MenusdhfashfjState(rx.State):
#     lists: list[dict] = [{"hello": "world"},{"hello": "world"},{"hello": "world"},{"hello": "world"},{"hello": "world"},{"hello": "world"},{"hello": "world"}]


def Menu() -> rx.Component:

    # lists = [{"hello": "world"},{"hello": "world"},{"hello": "world"},{"hello": "world"},{"hello": "world"},{"hello": "world"},{"hello": "world"}]
    return rx.cond(
        AuthState.is_menu,
        rx.chakra.box(
            rx.foreach(AuthState.menu, MenuItem),
            class_name="Menu grow flex flex-wrap justify-evenly px-2 overflow-y-scroll",
        ),
        rx.text("Loading..."),
    )
