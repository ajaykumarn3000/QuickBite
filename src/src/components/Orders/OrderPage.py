import reflex as rx
from src.components.Orders.Order import Order


def Orders(AuthState) -> rx.Component:
    return rx.box(
        rx.foreach(AuthState.orders, Order),
        class_name="Orders flex flex-wrap p-4 pt-2 gap-4",
    )
