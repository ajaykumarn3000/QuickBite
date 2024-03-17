import reflex as rx
from src.state import AuthState


def CartItem(item: dict) -> rx.Component:
    return rx.chakra.box(
        rx.chakra.image(
            src=item["icon"],
            class_name="object-cente object-cover aspect-video w-40 rounded-lg shadow",
        ),
        rx.chakra.box(
            rx.chakra.text(
                item["name"],
                class_name="text-center font-semibold text-xl transition-all text-gray-500",
            ),
            rx.chakra.box(
                rx.chakra.button(
                    rx.icon(
                        tag="minus",
                        class_name="material-symbols-rounded text-2xl rounded-full border-2  leading-none border-gray-500 text-gray-500",
                    ),
                    class_name="mx-2 flex items-center",
                    padding="0px",
                    background="none",
                    on_click=lambda: AuthState.remove_from_cart(item["id"]),
                ),
                rx.chakra.text(
                    item["quantity"],
                    class_name="border-2 rounded-lg  font-bold px-5 cursor-default border-gray-500 text-gray-500",
                ),
                rx.chakra.button(
                    rx.icon(
                        tag="plus",
                        class_name="material-symbols-rounded text-2xl rounded-full border-2  leading-none border-gray-500 text-gray-500",
                    ),
                    class_name="mx-2 flex items-center",
                    padding="0px",
                    background="none",
                    on_click=lambda: AuthState.add_to_cart(item["id"]),
                ),
                class_name="flex justify-center items-center w-full",
            ),
            class_name="grow my-1 ml-3 flex flex-col justify-evenly",
        ),
        rx.chakra.button(
            rx.icon(
                tag="x",
                class_name="material-symbols-rounded text-xl rounded-full bg-white/100 text-red-500 font-semibold leading-none border-gray-500 text-gray-500",
            ),
            class_name="m-1 absolute top-0 left-0",
            padding="0px",
            background="none",
            on_click=lambda: AuthState.delete_from_cart(item["id"]),
        ),
        class_name="CartItems relative flex p-2 transition-colors bg-white",
    )
