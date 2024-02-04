import reflex as rx
from src.components.Auth.FormInput import FormInput
from src.components.Auth.Button import Button


class RegisterState:
    otp = False

    def toggle_otp(self):
        self.otp = not self.otp


def Register(state) -> rx.Component:
    email = FormInput("Email", "email")
    password = FormInput("Password", "password")
    otp = FormInput("OTP", "number")
    submit_button = Button(rx.cond(RegisterState.otp, "Register", "Send OTP"), "submit")
    return \
        rx.box(
            rx.box(
                rx.form(
                    rx.text(
                        "Register",
                        class_name="text-accent text-3xl mb-2 font-semibold"
                    ),
                    rx.box(
                        rx.box(
                            email.render(
                                "text-gray-700 font-semibold tracking-wide text-lg border-solid boder-2 focus:bg-accent-100 focus:border-accent transition-colors duration-300 rounded-md"
                            ),
                            password.render(
                                "text-gray-700 font-semibold tracking-wide text-lg border-solid boder-2 focus:bg-accent-100 focus:border-accent transition-colors duration-300 rounded-md"
                            ),
                            class_name=rx.cond(RegisterState.otp, "email-password", "email-password Active")
                        ),
                        rx.box(
                            otp.render(
                                "text-center tracking-widest text-gray-700 font-semibold text-lg bg-background-200 border-solid boder-2 focus:bg-accent-100 focus:border-accent transition-colors duration-300 rounded-md"
                            ),
                            class_name=rx.cond(RegisterState.otp, "otp Active", "otp"),
                        ),
                        class_name="inputContainer"
                    ),

                    submit_button.render(
                        "btn flex relative justify-center items-center self-center text-background font-bold rounded-lg transition-colors duration-300 border-1 mt-4 bg-accent-400 shadow-md hover:bg-accent-450 active:bg-accent-500 active:shadow-none"
                    ),
                    class_name="mobileBox shadow-lg sm:shadow-none flex flex-col"
                ),
                rx.box(
                    "Already have an account? ",
                    rx.button("Login", class_name="ml-4 text-accent-600", on_click=state.toggle_login),
                    class_name="SwipeArea w-full py-4 text-gray-500 font-bold text-lg"
                ),
                class_name="AuthContainer"
            ),
            class_name=rx.cond(state.login, "Register Active", "Register")
        )
