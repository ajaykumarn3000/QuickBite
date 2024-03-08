import reflex as rx

# Comp
import src.components.Auth.Login as Login
import src.components.Auth.Register as Register


def Auth(AuthState) -> rx.Component:
    return rx.chakra.box(
        rx.chakra.box(
            Login.Login(AuthState),
            Register.Register(AuthState),
            Overlay(AuthState),
            class_name="UserAuth bg-background shadow-lg rounded-xl",
        ),
        class_name="h-screen flex justify-center items-center bg-gray-100",
    )


def Overlay(AuthState) -> rx.Component:
    return rx.chakra.box(
        rx.chakra.box(
            rx.chakra.box(
                rx.chakra.text(
                    "Create a Account", class_name="font-bold text-3xl mb-3"
                ),
                rx.chakra.text("Enter your personal details and start journey with us"),
                rx.chakra.button(
                    "SignIn",
                    class_name="GhostButton mt-2 border-2 border-white px-8 py-2 rounded-full bg-transparent font-semibold hover:underline",
                    background="auto",
                    _hover={"background_color": "auto"},
                    on_click=AuthState.toggle_login,
                ),
                class_name=rx.cond(
                    AuthState.login, "Left OverlayPanel Active", "Left OverlayPanel"
                ),
            ),
            rx.chakra.box(
                rx.chakra.text("Welcome Back!", class_name="font-bold text-3xl mb-3"),
                rx.chakra.text(
                    "To keep connected with us please login with your personal info"
                ),
                rx.chakra.button(
                    "Sign Up",
                    class_name="GhostButton mt-2 border-2 border-white px-8 py-2 rounded-full bg-transparent font-semibold hover:underline",
                    background="auto",
                    _hover={"background_color": "auto"},
                    on_click=AuthState.toggle_login,
                ),
                class_name=rx.cond(
                    AuthState.login, "Right OverlayPanel Active", "Right OverlayPanel"
                ),
            ),
            class_name=rx.cond(
                AuthState.login, "Overlay Active bg-accent", "Overlay bg-primary"
            ),
        ),
        class_name=rx.cond(
            AuthState.login, "OverlayContainer Active", "OverlayContainer"
        ),
    )
