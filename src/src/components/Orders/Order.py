import reflex as rx
from src.components.Orders.OrderInfo import OrderInfo


def Order(order: dict[bool, str, str, list[dict[int, str, int, int]]]) -> rx.Component:
    return rx.box(
        rx.box(
            rx.cond(
                order["successful"],
                rx.box(),
                rx.box(
                    rx.image(
                        src="https://www.pngall.com/wp-content/uploads/2/QR-Code-PNG-HD-Image.png",
                        class_name="max-w-20 max-h-20",
                    ),
                    rx.text(221077, class_name="font-bold text-sm"),
                    class_name="OrderCode text-center ml-2 flex flex-col justify-center",
                ),
            ),
            OrderInfo(order["orderList"]),
            class_name=rx.cond(
                order["successful"],
                "p-2 bg-white flex gap-4",
                "p-2 bg-white flex gap-4 min-w-72",
            ),
        ),
        rx.box(
            rx.text(order["time"]),
            rx.text(order["date"]),
            writing_mode="vertical-lr",
            transform="rotate(180deg)",
            class_name="flex gap-2 text-sm font-semibold text-gray-500 px-1 py-2 bg-gray-200",
        ),
        class_name="Order flex rounded-md overflow-hidden shadow-md",
    )
