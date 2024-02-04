import reflex as rx
# Comp
import src.components.Auth.Login as Login
import src.components.Auth.Register as Register


class AuthState(rx.State):
    login = True

    def toggle_login(self):
        self.login = not self.login


def Auth() -> rx.Component:
    return rx.box(
        rx.box(
            Login.Login(AuthState),
            Register.Register(AuthState),
            Overlay(),
            class_name="UserAuth bg-background shadow-lg rounded-xl"
        ),
        class_name="h-screen flex justify-center items-center"

    )


def Overlay() -> rx.Component:
    print(type(AuthState.login))
    return \
        rx.box(
            rx.box(
                rx.box(
                    rx.text("Create a Account",
                            class_name="font-bold text-3xl mb-3"
                            ),
                    rx.text("Enter your personal details and start journey with us"),
                    rx.button("SignIn",
                              class_name="GhostButton mt-2 border-2 border-white px-8 py-2 rounded-full bg-transparent font-semibold hover:underline",
                              background="auto", _hover={"background_color": "auto"}, on_click=AuthState.toggle_login),
                    class_name=rx.cond(AuthState.login, "Left OverlayPanel Active", "Left OverlayPanel")
                ),
                rx.box(
                    rx.text("Welcome Back!",
                            class_name="font-bold text-3xl mb-3"
                            ),
                    rx.text("To keep connected with us please login with your personal info"),
                    rx.button("Sign Up",
                              class_name="GhostButton mt-2 border-2 border-white px-8 py-2 rounded-full bg-transparent font-semibold hover:underline",
                              background="auto", _hover={"background_color": "auto"}, on_click=AuthState.toggle_login),
                    class_name=rx.cond(AuthState.login, "Right OverlayPanel Active", "Right OverlayPanel")
                ),
                class_name=rx.cond(AuthState.login, "Overlay Active bg-accent", "Overlay bg-primary")
            ),
            class_name=rx.cond(AuthState.login, "OverlayContainer Active", "OverlayContainer")
        )
