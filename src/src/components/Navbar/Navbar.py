import reflex as rx
from src.components.Navbar.Dropdown import Dropdown


def Navbar() -> rx.Component:
    return rx.box(
        rx.link(
            "Quickbite",
            href="/",
            class_name="text-primary-500 hover:text-primary-600 text-2xl font-semibold",
        ),
        Dropdown(),
        class_name="Navbar flex w-full justify-between items-center px-2 py-1 shadow bg-white mb-2",
    )
