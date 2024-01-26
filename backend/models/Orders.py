import os
from copy import deepcopy
from sqlite3 import InternalError

from models.Cart import Cart
from models.MenuCard import MenuCard
from sqlalchemy.orm import declarative_base, Session
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


def crosscheck_cart_items_in_menu(user_id: int):
    """Checkout the user's cart"""
    items_requiring_modification = []
    try:
        for cart_item in Cart(user_id).cart.all():
            MenuCard.get_item(cart_item.item_id).item_quantity -= cart_item.quantity
        database.commit()
    except InternalError:  # Should occur when item is no longer available
        database.rollback()
        items_requiring_modification.append(
            {
                "item": cart_item.item_name
            }
        )
    else:
        return None
    finally:
        return items_requiring_modification


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
