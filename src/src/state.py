import reflex as rx
from src.controller.menuController import getMenu
from src.controller.cartController import getCart
from src.setup import TOKEN as token


# Auth
class AuthState(rx.State):
    login = False
    token: str = ""
    logged_in: bool = False
    # token: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3R5cGUiOiJ1c2VyIiwidWlkIjoiMjIxMDc3IiwiZXhwIjoxNzA5NjUxOTc0fQ.EnNiTm3L1ARPB8722w9xAFkEmt2X47q3bqhsU0kUAxQ"
    # logged_in: bool = True

    def toggle_login(self):
        self.login = not self.login

    def toggle_logged_in(self):
        self.logged_in = self.token != ""

    def set_token(self, token: str):
        self.token = token
        self.toggle_logged_in()

    def login_handle_submit(self, form_data: dict):
        from src.controller.authController import login

        if form_data["UID"] and form_data["Password"]:
            data = {"uid": form_data["UID"], "passcode": form_data["Password"]}
            print("Hello world")
            self.set_token(login(data))


    register_otp = False

    def register_toggle_otp(self):
        self.register_otp = not self.register_otp

    def register_handle_submit(self, form_data: dict):
        from src.controller.authController import register, verify_otp

        if not self.register_otp and form_data["Email"] and form_data["Password"]:
            data = {"passcode": form_data["Password"]}
            if "@student.sfit.ac.in" in form_data["Email"]:
                data["username"] = form_data["Email"].replace("@student.sfit.ac.in", "")
            elif "@sfit.ac.in" in form_data["Email"]:
                data["username"] = form_data["Email"].replace("@student.sfit.ac.in", "")
            else:
                return
            if register(data):
                self.register_toggle_otp()
        elif self.register_otp and form_data["Email"] and form_data["OTP"]:
            data = {"email": form_data["Email"], "otp": str(form_data["OTP"])}
            self.set_token(verify_otp(data))

    def logout(self):
        self.token = ""
        self.toggle_logged_in()

class MenuState(rx.State):
    menu: list[dict] = getMenu(AuthState.token)


class MenuItemState(rx.State):

    selected = False

    def select(self):
        self.selected = True

    def deselect(self):
        self.selected = False


class CartState(rx.State):
    show_info = False
    show_cart = False
    cart: list[dict] = getCart(token)

    def toggle_cart(self):
        self.show_cart = not self.show_cart

    def toggle_info(self):
        self.show_info = not self.show_info

    def add_to_cart(self, item: dict):
        self.cart.append(item)

    def remove_from_cart(self, item: dict):
        self.cart.remove(item)

    def clear_cart(self):
        self.cart = []

    @rx.var
    def total(self):
        total = 0
        for item in self.cart:
            total += item["price"] * item["quantity"]
        return total
