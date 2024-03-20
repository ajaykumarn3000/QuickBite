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
            self.order_id = ""

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

    # ORders
    orders: list[dict[bool, str, str, list[dict[int, str, int, int]]]] = [
        {
            "successful": False,
            "time": "10:45 AM",
            "date": "20/01/24",
            "orderList": [
                {"id": 1, "name": "Burger", "quantity": 2, "price": 100},
                {"id": 2, "name": "Pizza", "quantity": 1, "price": 200},
                {"id": 3, "name": "Pasta", "quantity": 1, "price": 150},
            ],
        },
        {
            "successful": False,
            "time": "10:45 AM",
            "date": "20/01/24",
            "orderList": [
                {"id": 1, "name": "Burger", "quantity": 2, "price": 100},
                {"id": 2, "name": "Pizza", "quantity": 1, "price": 200},
                {"id": 3, "name": "Pasta", "quantity": 1, "price": 150},
            ],
        },
        {
            "successful": False,
            "time": "10:45 AM",
            "date": "20/01/24",
            "orderList": [
                {"id": 1, "name": "Burger", "quantity": 2, "price": 100},
                {"id": 2, "name": "Pizza", "quantity": 1, "price": 200},
                {"id": 3, "name": "Pasta", "quantity": 1, "price": 150},
            ],
        },
        {
            "successful": True,
            "time": "11:45 AM",
            "date": "20/01/24",
            "orderList": [
                {"id": 1, "name": "Burger", "quantity": 2, "price": 100},
                {"id": 2, "name": "Pizza", "quantity": 1, "price": 200},
                {"id": 3, "name": "Pasta", "quantity": 1, "price": 150},
            ],
        },
        {
            "successful": True,
            "time": "11:45 AM",
            "date": "20/01/24",
            "orderList": [
                {"id": 1, "name": "Burger", "quantity": 2, "price": 100},
                {"id": 2, "name": "Pizza", "quantity": 1, "price": 200},
                {"id": 3, "name": "Pasta", "quantity": 1, "price": 150},
            ],
        },
        {
            "successful": True,
            "time": "11:45 AM",
            "date": "20/01/24",
            "orderList": [
                {"id": 1, "name": "Burger", "quantity": 2, "price": 100},
                {"id": 2, "name": "Pizza", "quantity": 1, "price": 200},
                {"id": 3, "name": "Pasta", "quantity": 1, "price": 150},
            ],
        },
        {
            "successful": True,
            "time": "12:45 AM",
            "date": "20/01/24",
            "orderList": [
                {"id": 1, "name": "Burger", "quantity": 2, "price": 100},
                {"id": 2, "name": "Pizza", "quantity": 1, "price": 200},
                {"id": 3, "name": "Pasta", "quantity": 1, "price": 150},
                {"id": 4, "name": "Pasta", "quantity": 1, "price": 150},
            ],
        },
    ]

    order_id: str = ""

    @rx.var
    def is_orders(self) -> bool:
        return self.order_id != ""

    def get_order_id(self):
        response = requests.post(
            f"{SERVER_URL}/user/api/cart/checkout",
            headers={"Authorization": f"Bearer {self.token}"},
        )
        if response.ok:
            self.order_id = response.json()

    @rx.var
    def get_payment_url(self) -> str:
        return f"{SERVER_URL}/user/api/cart/checkout/{self.order_id}"
class CartState(rx.State):
    pass
