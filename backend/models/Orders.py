from copy import deepcopy

from sqlalchemy import (
    Column,
    String,
    Integer,
    PrimaryKeyConstraint,
)

from database import conn as database, Base, engine
from models.Cart import Cart
from models.MenuCard import get_item_name_by_item_id
from models.Users import User


class Payments(Base):
    __tablename__ = "payments"
    payment_id = Column(String, primary_key=True)
    payment_amount = Column(String, nullable=False)
    payment_status = Column(String, nullable=False)
    payment_method = Column(String, nullable=False)
    payment_timestamp = Column(String, nullable=False)
    order_id = Column(String, nullable=False, unique=True)

    def __init__(
            self,
            order_id: str,
            payment_id: str,
            payment_amount: str,
            payment_status: str,
            payment_method: str,
            payment_timestamp: str
    ):
        self.order_id = order_id
        self.payment_id = payment_id
        self.payment_amount = payment_amount
        self.payment_status = payment_status
        self.payment_method = payment_method
        self.payment_timestamp = payment_timestamp
        database.add(self)
        database.commit()


def get_all_orders(user_id: int = None):
    orders = list()
    if user_id is None:
        users = database.query(User).all()
        user_orders = list()
        for user in users:
            print(user)
            records = database.query(Orders).filter_by(user_id=user.uid).all()
            orders = list()
            for record in records:
                order = {
                    "item_id": record.item_id,
                    "item_name": record.name,
                    "item_quantity": record.quantity
                }
                orders.append(order)
            user_orders.append({"user_id": user.uid, "items": orders})
        return user_orders
    records = database.query(Orders).filter_by(user_id=user_id).all()
    for record in records:
        order = {
            "item_id": record.item_id,
            "item_name": record.name,
            "item_quantity": record.quantity
        }
        orders.append(order)
    return orders


def serve_order(user_id: int):
    try:
        database.query(Orders).filter_by(user_id=user_id).delete()
        database.commit()
        return f"All orders of {user_id} has been served!"
    except Exception as e:
        database.rollback()
        raise e

class Orders(Base):
    __tablename__ = "orders"
    order_id = Column(String, nullable=False)
    cart_id = Column(String, nullable=False)
    user_id = Column(Integer, nullable=False)
    item_id = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    PrimaryKeyConstraint(order_id, cart_id)

    def __init__(self, user_id: int, order_id: str):
        for cart_item in Cart(user_id).cart.all():
            self.order_id = order_id
            self.user_id = cart_item.user_id
            self.cart_id = cart_item.cart_id
            self.item_id = cart_item.item_id
            self.name = get_item_name_by_item_id(self.item_id)
            self.quantity = cart_item.quantity
            database.add(deepcopy(self))
        database.commit()

    def __repr__(self):
        return f"<Orders(order_id={self.order_id}, cart_id={self.cart_id})>"


Base.metadata.create_all(bind=engine, checkfirst=True)
