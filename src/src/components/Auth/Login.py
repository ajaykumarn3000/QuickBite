import reflex as rx
from src.components.Auth.FormInput import FormInput
from src.components.Auth.Button import Button
from src.controller.authController import login


def Login(state) -> rx.Component:
    uid = FormInput("UID", "number")
    password = FormInput("Password", "password")
    submit_button = Button("Login", "submit")

    return rx.chakra.box(
        rx.chakra.box(
            rx.chakra.form(
                rx.chakra.text(
                    "Login", class_name="text-primary text-3xl mb-2 font-semibold"
                ),
                uid.render(
                    "text-gray-700 font-semibold tracking-wider text-lg border-solid boder-2 "
                    "focus:bg-primary-100 focus:border-primary transition-colors duration-300 rounded-md"
                    "border-white bg-background-200"
                ),
                password.render(
                    "text-gray-700 font-semibold tracking-wide text-lg border-solid boder-2 focus:bg-primary-100 "
                    "focus:border-primary transition-colors duration-300 rounded-md"
                    "border-white bg-background-200"
                ),
                submit_button.render(
                    "btn flex relative justify-center items-center self-center text-background font-bold"
                    " rounded-lg transition-colors duration-300 border-1 mt-4 bg-primary-400 shadow-md "
                    "hover:bg-primary-450 active:bg-primary-500 active:shadow-none"
                ),
                class_name="mobileBox shadow-lg sm:shadow-none flex flex-col",
                on_submit=state.login_handle_submit,
            ),
            rx.chakra.box(
                "New to Quickbite? ",
                rx.chakra.button(
                    "Register",
                    class_name="ml-4 text-primary-500",
                    on_click=state.toggle_login,
                ),
                class_name="SwipeArea w-full py-4 text-gray-500 font-bold text-lg",
            ),
            class_name="AuthContainer",
        ),
        class_name=rx.cond(state.login, "Login Active", "Login"),
    )
