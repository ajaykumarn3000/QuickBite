import os
import secrets
import razorpay
from models.Users import User
from models.MenuCard import MenuCard
from datetime import datetime, timedelta
from database import conn as database, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.exc import IntegrityError, NoResultFound, InternalError

client = razorpay.Client(auth=(os.environ['KEY_ID'], os.environ['KEY_SECRET']))
client.set_app_details({"title": "QuickBite CMS - SFIT", "version": "1.0.0"})


def validate_cart_items(user_id: int) -> list[dict]:
    """Verify whether the items in the cart are available in the menu or not"""
    items_to_modify = []
    for cart_item in Cart(user_id).cart.all():
        item_in_menu = MenuCard.get_item(MenuCard, cart_item.item_id)
        if item_in_menu.item_quantity - cart_item.quantity < 0:
            items_to_modify.append(
                {
                    "id": cart_item.item_id,
                    "item": item_in_menu.item_name,
                    "quantity in cart": cart_item.quantity,
                    "quantity available in menu": item_in_menu.item_quantity,
                }
            )
    if items_to_modify:
        return items_to_modify
    else:
        for cart_item in Cart(user_id).cart.all():
            database.query(MenuCard).filter_by(
                item_id=cart_item.item_id
            ).one().item_quantity -= cart_item.quantity
        database.commit()


class Cart(Base):
    __tablename__ = "cart"
    cart_id = Column(String, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.uid), nullable=False)
    item_id = Column(Integer, ForeignKey(MenuCard.item_id), nullable=False)
    quantity = Column(Integer, nullable=False)

    def __init__(self, user_id: int, item_id: int = None, quantity: int = None):
        self.user_id = user_id
        self.item_id = item_id
        self.quantity = quantity
        self.latest_razorpay_order_id = None
        # TODO: Update self.cart after every operation
        self.cart = database.query(Cart).filter_by(user_id=self.user_id)

    def __repr__(self):
        user_id = self.user_id
        item_id = self.item_id
        quantity = self.quantity
        return f"<Cart(cart_id={self.cart_id})>"

    def get_cart(self) -> list[dict]:  # To be only used to display item_id, quantity pair
        items = []
        for cart_item in self.cart.all():
            menu_item = database.get(MenuCard, cart_item.item_id)
            items.append(
                {
                    "id": cart_item.item_id,
                    "name": menu_item.item_name,
                    "quantity": cart_item.quantity,
                    "price": menu_item.item_price,
                    "icon": menu_item.item_icon
                }
            )
        return items

    def pay(self):
        """Pay for the items in cart"""
        amount = 0
        order_list = []
        now = datetime.utcnow() + timedelta(hours=5, minutes=30)
        for cart_item in self.cart.all():
            menu_item = MenuCard.get_item(MenuCard, item_id=cart_item.item_id)
            total_item_price = menu_item.item_price * cart_item.quantity
            amount += total_item_price
            order_details = dict()
            order_details["id"] = cart_item.item_id
            order_details["name"] = menu_item.item_name
            order_details["quantity"] = cart_item.quantity
            order_details["price"] = total_item_price
            order_list.append(order_details)
        data = {
            "amount": amount * 100,
            "currency": "INR",
            "receipt": secrets.token_hex(3),
            "notes": {
                "time": now.strftime("%I:%M %p"),
                "date": now.strftime("%d/%m/%y")
            }
        }
        payment = client.order.create(data=data)
        self.latest_razorpay_order_id = payment['id']
        payment['orderList'] = order_list
        return payment

    def verify_payment(self, payment_id: str, payment_signature: str):
        """Verify the payment"""
        return client.utility.verify_payment_signature({
            'razorpay_order_id': self.latest_razorpay_order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': payment_signature
        })

    def item_exists(self, item_id: int):
        """Check if an item exists in the database, for that particular user"""
        return self.cart.filter_by(item_id=item_id).first()

    def add_item(self, item: int):
        try:
            existing_item = self.item_exists(item)
            if existing_item:  # If item exists, increment its quantity by 1
                existing_item.quantity += 1
            else:  # Else, append the item to the cart with quantity 1
                self.cart_id = secrets.token_hex(3)
                self.item_id = item
                self.quantity = 1
                database.add(self)
            database.commit()
            self.cart = database.query(Cart).filter_by(user_id=self.user_id)
        except IntegrityError:  # Occurs when the item is not in the menu
            database.rollback()
            raise Exception("Item does not exist in the menu")
        except InternalError:  # Occurs when item requested is more than in menu
            database.rollback()
            raise Exception("Quantity exceeds available quantity in Menu!")

    def remove_item(self, item: int):
        try:
            # There should be only one and only one item existing in the cart
            existing = self.cart.filter_by(item_id=item).one()
            existing.quantity -= 1
            print("Before committing, quantity is ", existing.quantity)
            database.commit()
            self.cart = database.query(Cart).filter_by(user_id=self.user_id)
        except NoResultFound:  # if the item does not exist in the cart
            raise Exception("Item does not exist in the cart")
        except IntegrityError: # if the item quantity in cart is zero
            database.rollback()
            self.delete_item(existing.quantity)

    def delete_item(self, item: int):
        # TODO: Raise Exception if item does not exist in the cart
        existing = self.cart.filter_by(item_id=item)
        existing.delete()
        database.commit()
        self.cart = database.query(Cart).filter_by(user_id=self.user_id)
