import reflex as rx
from src.controller.menuController import getMenu
from src.setup import TOKEN as token


# Auth
class AuthState(rx.State):
    login = False

    def toggle_login(self):
        self.login = not self.login


class LoginState(rx.State):
    form_data = {}

    def handle_submit(self, form_data: dict):
        from src.controller.authController import login

        if form_data["UID"] and form_data["Password"]:
            data = {"uid": form_data["UID"], "passcode": form_data["Password"]}
            login(data)


class RegisterState(rx.State):
    otp = False
    form_data = {}

    def toggle_otp(self):
        self.otp = not self.otp

    def handle_submit(self, form_data: dict):
        from src.controller.authController import register, verify_otp

        if not self.otp and form_data["Email"] and form_data["Password"]:
            data = {"passcode": form_data["Password"]}
            if "@student.sfit.ac.in" in form_data["Email"]:
                data["username"] = form_data["Email"].replace("@student.sfit.ac.in", "")
            elif "@sfit.ac.in" in form_data["Email"]:
                data["username"] = form_data["Email"].replace("@student.sfit.ac.in", "")
            else:
                return
            if register(data):
                self.toggle_otp()
        elif self.otp and form_data["Email"] and form_data["OTP"]:
            data = {"email": form_data["Email"], "otp": str(form_data["OTP"])}
            if verify_otp(data):
                self.toggle_otp()


class MenuState(rx.State):
    menu: list[dict] = getMenu(token)


class MenuItemState(rx.State):

    selected = False

    def select(self):
        self.selected = True

    def deselect(self):
        self.selected = False

class CartState(rx.State):
    show_info = False
    show_cart = False
    cart: list[dict] = []

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
            total += (item["price"]*item["quantity"])
        return total


