import reflex as rx
from src.setup import SERVER_URL
import requests


# Auth
class AuthState(rx.State):
    login = False
    token: str = rx.LocalStorage(name="token")

    @rx.var
    def is_logged_in(self) -> bool:
        if self.token != "":
            self.get_cart()
            self.get_menu()
            return True
        return False

    def toggle_login(self):
        self.login = not self.login

    def toggle_logged_in(self):
        self.logged_in = self.token != ""

    def set_token(self, token: str):
        self.token = token

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

    menu: list[dict] = []

    @rx.var
    def is_menu(self) -> bool:
        return self.menu != []

    # menu

    def get_menu(self) -> list[dict]:
        if not self.token:
            return
        response = requests.get(
            f"{SERVER_URL}/kitchen/menu",
            headers={"Authorization": f"Bearer {self.token}"},
        )

        if response.ok:
            print(response.json())
            self.menu = response.json()
            # return response.json()
        # return None

    # cart
    show_info = True
    show_cart = False
    cart: list[dict] = []

    @rx.var
    def is_cart(self) -> bool:
        return self.cart != []

    def get_cart(self) -> list[dict]:
        if not self.token:
            return
        response = requests.get(
            f"{SERVER_URL}/user/api/cart",
            headers={"Authorization": f"Bearer {self.token}"},
        )
        if response.ok:
            self.total = 0
            data = response.json()
            for item in data:
                item["total"] = item["price"] * item["quantity"]
            self.cart = data

    def toggle_cart(self):
        self.show_cart = not self.show_cart

    def toggle_info(self):
        self.show_info = not self.show_info

    @rx.var
    def total(self):
        total = 0
        for item in self.cart:
            total += item["price"] * item["quantity"]
        return total

    def add_to_cart(self, item_id: int):
        print(item_id)
        response = requests.post(
            f"{SERVER_URL}/user/api/cart/add/{item_id}",
            headers={"Authorization": f"Bearer {self.token}"},
        )
        if response.ok:
            self.get_cart()

    def remove_from_cart(self, item_id: int):
        response = requests.post(
            f"{SERVER_URL}/user/api/cart/remove/{item_id}",
            headers={"Authorization": f"Bearer {self.token}"},
        )
        if response.ok:
            self.get_cart()

    def delete_from_cart(self, item_id: int):
        response = requests.delete(
            f"{SERVER_URL}/user/api/cart/delete/{item_id}",
            headers={"Authorization": f"Bearer {self.token}"},
        )
        if response.ok:
            self.get_cart()


class CartState(rx.State):
    pass


#     show_info = False
#     show_cart = False
#     cart: list[dict] = getCart(token)

#     def toggle_cart(self):
#         self.show_cart = not self.show_cart

#     def toggle_info(self):
#         self.show_info = not self.show_info

#     def add_to_cart(self, item: dict):
#         self.cart.append(item)

#     def remove_from_cart(self, item: dict):
#         self.cart.remove(item)

#     def clear_cart(self):
#         self.cart = []

#     @rx.var
#     def total(self):
#         total = 0
#         for item in self.cart:
#             total += item["price"] * item["quantity"]
#         return total
