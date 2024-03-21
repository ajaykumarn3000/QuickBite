import reflex as rx


def Success() -> rx.Component:
    return rx.box(
        rx.box(
            rx.box(
                rx.box(
                    rx.icon(tag="check", class_name="w-12 h-12"),
                    class_name="rounded-full bg-primary-500 p-2 text-white text-3xl font-bold",
                ),
                class_name="flex justify-center items-center w-20 h-20",
            ),
            rx.text("Order Successful", class_name="text-3xl font-bold"),
            rx.button(
                "Back to Home",
                class_name="mt-[1rem] bg-primary-500 text-white font-bold text-lg px-[2rem] py-[1rem] rounded",
                background_color="#00a878",
                on_click=rx.redirect("/"),
            ),
            class_name="flex flex-col items-center bg-white rounded-lg shadow px-[1.5rem] py-[4rem]",
        ),
        class_name="h-screen w-full flex justify-center items-center bg-primary-500",
    )
