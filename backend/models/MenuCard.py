# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String
from sqlalchemy.exc import IntegrityError
from database import conn as database, Base, engine


def item_exists(item_name: str) -> bool:
    """Check if an item exists in the database, by querying its name"""
    return bool(database.query(MenuCard).filter_by(item_name=item_name).all())


def get_item_name_by_item_id(item_id: int) -> str:
    """Function which returns the name of the item"""
    return database.query(MenuCard).filter_by(item_id=item_id).all()[0].item_name


class MenuCard(Base):
    """Table which represents all the items which can be made in the canteen"""

    __tablename__ = "menu"
    # The uid is created by an auto incrementing the database key
    item_id = Column(Integer, primary_key=True, autoincrement=True)
    # The name of the item on the menu
    item_name = Column(String, unique=True, nullable=False)
    # The quantity of the item on the menu, empty if the item was not made today
    item_quantity = Column(Integer)
    # The price of the item on the menu for one serving
    item_price = Column(Integer, nullable=False)
    # The category of the item on the menu
    item_type = Column(String, nullable=False)
    # The image of the item on the menu
    item_icon = Column(String)

    def __init__(
            self,
            name: str,
            type: str,
            icon: str,
            quantity: int,
            price: int,
            category: str
    ):
        """Code to be executed when a new item is instantiated"""
        self.item_name = name
        self.item_type = type
        self.item_icon = icon
        self.item_quantity = quantity
        self.item_price = price
        self.item_type = category

    def get_all_items(self) -> list[dict]:
        """Get all the items from the database"""
        items = []
        for item in database.query(MenuCard).order_by(MenuCard.item_id).all():
            items.append(
                {
                    "item_id": item.item_id,
                    "item_name": item.item_name,
                    "item_type": item.item_type,
                    "item_icon": item.item_icon,
                    "item_price": item.item_price,
                    "item_quantity": item.item_quantity
                }
            )
        return items

    def get_item(self, item_id):
        return database.query(MenuCard).filter_by(item_id=item_id).one()

    def add_item(self) -> None:
        """Add a new item to the database"""
        database.add(self)
        database.commit()

    def edit_item(self, item_id, item_details: dict) -> None:
        """Edit the price and/or quantity of an existing menu item"""
        menu_item = MenuCard.get_item(self, item_id)
        try:
            for key, value in item_details.items():
                setattr(menu_item, key, value)
            database.commit()
        except IntegrityError:
            database.rollback()
            raise Exception("All fields should be non zero")

    def delete_item(self, item_id: int) -> None:
        try:
            database.query(MenuCard).filter_by(item_id=item_id).delete()
            database.commit()
        except Exception as e:
            database.rollback()
            raise e


Base.metadata.create_all(bind=engine, checkfirst=True)
