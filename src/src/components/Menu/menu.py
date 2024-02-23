import reflex as rx
from src.components.Menu.menu_item import MenuItem

from src.state import MenuState
# class MenusdhfashfjState(rx.State):
#     lists: list[dict] = [{"hello": "world"},{"hello": "world"},{"hello": "world"},{"hello": "world"},{"hello": "world"},{"hello": "world"},{"hello": "world"}]


def Menu() -> rx.Component:
    # lists = [{"hello": "world"},{"hello": "world"},{"hello": "world"},{"hello": "world"},{"hello": "world"},{"hello": "world"},{"hello": "world"}]
    return rx.box(
        rx.foreach(MenuState.menu, MenuItem),
        class_name="Menu grow flex flex-wrap justify-evenly px-2 overflow-y-scroll",
    )
