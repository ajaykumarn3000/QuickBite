# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, Column, INTEGER, TEXT
from sqlalchemy.orm import declarative_base, Session

# The path to the database file
DATABASE = 'database/database.db'

# Instantiate the ORM of the database to a python object
Base = declarative_base()
# Create a connection to a database using its file path
engine = create_engine(f'sqlite:///{DATABASE}')
# A session to connect to the database connection
database = Session(bind=engine)


def item_exists(item_name: str) -> bool:
    """Check if an item exists in the database, by querying its name"""
    return bool(database.query(MenuCard).filter_by(item_name=item_name).all())


class MenuCard(Base):
    """Table which represents all the items which can be made in the canteen"""
    __tablename__ = 'MenuCard'
    # The uid is created by an auto incrementing the database key
    item_id = Column(INTEGER, primary_key=True, autoincrement=True)
    # The name of the item on the menu
    item_name = Column(TEXT, unique=True, nullable=False)
    # The quantity of the item on the menu, empty if the item was not made today
    item_quantity = Column(INTEGER)
    # The price of the item on the menu for one serving
    item_price = Column(INTEGER, nullable=False)
    # The category of the item on the menu
    item_type = Column(TEXT, nullable=False)

    def __init__(self, name: str, quantity: int, price: int, category: str):
        """Code to be executed when a new item is instantiated"""
        self.item_name: str = name
        self.item_quantity: int = quantity
        self.item_price: int = price
        self.item_type: str = category

    def get_items(self):
        """Get all the items from the database"""
        menu_card = database.query(MenuCard).all()
        items = [item.__dict__ for item in menu_card]
        for item in items:
            item.pop('_sa_instance_state', None)
        return items

    def add_item(self) -> None:
        """Add a new item to the database"""
        database.add(self)
        database.commit()


Base.metadata.create_all(engine, checkfirst=True)
