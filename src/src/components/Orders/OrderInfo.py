import reflex as rx


def renderOrder(order: dict[int, str, int, int]) -> rx.Component:
    return (
        rx.box(
            rx.text(order["name"]),
            rx.text("₹ " + str(order["quantity"] * order["price"])),
            class_name="gap-8 flex justify-between font-medium text",
        ),
    )


def OrderInfo(orderList: list[dict[int, str, int, int]]) -> rx.Component:
    return rx.box(
        # rx.foreach(orderList, renderOrder),
        rx.divider(),
        rx.box(
            rx.text("Total:"),
            rx.text("₹ " + str(10000)),
            class_name="gap-8 flex justify-between font-medium text text-lg",
        ),
        class_name="OrderInfo w-full mx-2 flex flex-col justify-around",
    )
