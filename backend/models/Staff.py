# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, Column, INTEGER, TEXT
from sqlalchemy.orm import declarative_base, Session
# from backend.logs.logger import logger


PATH_TO_DB = 'database/database.db'

Base = declarative_base()
engine = create_engine(f'sqlite://{PATH_TO_DB}')
session = Session(bind=engine)


class Staff(Base):
    """Table which represents all the possible items in the Inventory"""
    __tablename__ = 'Inventory'

    uid = Column(INTEGER, primary_key=True, autoincrement=True)
    password = Column(TEXT, nullable=False)
