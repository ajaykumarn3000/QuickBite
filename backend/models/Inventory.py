# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, Column, INTEGER, TEXT
from sqlalchemy.orm import declarative_base, sessionmaker
from backend.logs.logger import logger


PATH_TO_DB = '../backend/database/database.sqlite'

Base = declarative_base()
engine = create_engine(f'sqlite://{PATH_TO_DB}')
Session = sessionmaker(bind=engine)
session = Session()


class Inventory(Base):
    """Table which represents all the possible items in the Inventory"""
    __tablename__ = 'Inventory'

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(TEXT, nullable=False)

