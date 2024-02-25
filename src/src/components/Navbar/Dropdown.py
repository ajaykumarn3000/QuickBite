import reflex as rx


def Dropdown() -> rx.Component:
    return rx.menu(
        rx.menu_button(rx.icon(tag="hamburger"), class_name="text-2xl"),
        rx.menu_list(
            rx.menu_item("My Order", class_name=""),
            rx.menu_item("Settings", class_name=""),
            rx.menu_divider(),
            rx.menu_item("Logout", class_name="hover:text-red-500"),
        ),
    )
