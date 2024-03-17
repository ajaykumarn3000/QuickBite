from copy import deepcopy
from database import conn as database, Base
from models.Cart import Cart
from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    PrimaryKeyConstraint,
)


class Payments(Base):
    __tablename__ = "payments"
    payment_id = Column(String, primary_key=True)
    payment_amount = Column(String, nullable=False)
    payment_status = Column(String, nullable=False)
    payment_method = Column(String, nullable=False)
    payment_timestamp = Column(String, nullable=False)
    order_id = Column(Integer, nullable=False, autoincrement=True)


class Orders(Base):
    __tablename__ = "orders"
    order_id = Column(Integer, ForeignKey("payments.order_id"), nullable=False)
    cart_id = Column(String, ForeignKey(Cart.cart_id), nullable=False)
    PrimaryKeyConstraint(order_id, cart_id)

    def __init__(self, user_id: int):
        for cart_item in Cart(user_id).cart.all():
            self.cart_id = cart_item.cart_id
            database.add(deepcopy(self))
        database.commit()

    def __repr__(self):
        return f"<Orders(order_id={self.order_id}, cart_id={self.cart_id})>"
