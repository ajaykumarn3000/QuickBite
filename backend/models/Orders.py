import os
from copy import deepcopy
from sqlite3 import InternalError

from models.Cart import Cart
from models.MenuCard import MenuCard
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, PrimaryKeyConstraint

DB_CONNECTION_STRING = os.environ.get('DB_CONNECTION_STRING')
Base = declarative_base()
engine = create_engine(DB_CONNECTION_STRING)
database = Session(bind=engine)


class Payments(Base):
    __tablename__ = 'payments'
    payment_id = Column(String, primary_key=True)
    payment_amount = Column(String, nullable=False)
    payment_status = Column(String, nullable=False)
    payment_method = Column(String, nullable=False)
    payment_timestamp = Column(String, nullable=False)
    order_id = Column(Integer, nullable=False, autoincrement=True)


def validate_cart_items(user_id: int) -> list[dict]:
    """Verify whether the items in the cart are available in the menu or not"""
    items_to_modify = []
    for cart_item in Cart(user_id).cart.all():
        item_in_menu = MenuCard.get_item(MenuCard, cart_item.item_id)
        if item_in_menu.item_quantity - cart_item.quantity < 0:
            items_to_modify.append(
                {
                    "item": item_in_menu.item_name,
                    "quantity in cart": cart_item.quantity,
                    "quantity available in menu": item_in_menu.item_quantity
                }
            )
    if items_to_modify:
        print(items_to_modify)
        return items_to_modify
    else:
        for cart_item in Cart(user_id).cart.all():
            database.query(MenuCard).filter_by(item_id=cart_item.item_id).one().item_quantity -= cart_item.quantity
        database.commit()


class Orders(Base):
    __tablename__ = 'orders'
    order_id = Column(Integer, ForeignKey('payments.order_id'), nullable=False)
    cart_id = Column(String, ForeignKey(Cart.cart_id), nullable=False)
    PrimaryKeyConstraint(order_id, cart_id)

    def __init__(self, user_id: int):
        for cart_item in Cart(user_id).cart.all():
            self.cart_id = cart_item.cart_id
            database.add(deepcopy(self))
        database.commit()

    def __repr__(self):
        return f"<Orders(order_id={self.order_id}, cart_id={self.cart_id})>"


Base.metadata.create_all(bind=engine, checkfirst=True)
