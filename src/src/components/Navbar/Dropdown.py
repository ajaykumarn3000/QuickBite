import reflex as rx


def Dropdown(AuthState) -> rx.Component:
    return rx.menu.root(
        rx.menu.trigger(
            rx.button(
                rx.icon(tag="menu"),
                variant="ghost",
                class_name="text-2xl text-primary-500 hover:text-primary-500 p-2 transition-colors",
                color="teal",
                background="auto",
                _hover={"background": "auto"},
            ),
        ),
        rx.menu.content(
            rx.menu.item("My Order", class_name=""),
            rx.menu.item("Settings", class_name=""),
            rx.menu.separator(),
            rx.menu.item("Logout", class_name="hover:text-red-500", on_click=AuthState.logout)
        ),
    )
    # return rx.menu(
    #     rx.menu_button(rx.icon(tag="hamburger"), class_name="text-2xl"),
    #     rx.menu_list(
    #         rx.menu_item("My Order", class_name=""),
    #         rx.menu_item("Settings", class_name=""),
    #         rx.menu_divider(),
    #         rx.menu_item("Logout", class_name="hover:text-red-500"),
    #     ),
    # )
