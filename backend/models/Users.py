# -*- coding: utf-8 -*-
import logging
from bcrypt import gensalt, hashpw
from sqlalchemy import create_engine, Column, INTEGER, TEXT
from sqlalchemy.orm import declarative_base, sessionmaker

DB_PATH = 'database.sqlite'
DOMAIN = 'sfit.ac.in'

Base = declarative_base()
engine = create_engine(f'sqlite:///{DB_PATH}', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


class User:

    def __init__(self, uid: int, passcode: str) -> None:
        self.uid = uid
        self.passcode = passcode


class Student(User, Base):
    __tablename__ = 'student'
    domain = f'{__tablename__}.{DOMAIN}'
    uid = Column(INTEGER, primary_key=True)
    email = Column(TEXT, unique=True, nullable=False)
    passcode = Column(TEXT, nullable=False)

    def __init__(self, username: str, uid: int, passcode: str) -> None:
        hashed_password = hashpw(passcode.encode(), gensalt()).decode()
        super().__init__(uid, hashed_password)
        self.email = f'{username}@{Student.domain}'
        session.add(self)
        session.commit()


class Teacher(User, Base):
    __tablename__ = 'teacher'
    domain = f'@{DOMAIN}'
    uid = Column(INTEGER, primary_key=True)
    email = Column(TEXT, unique=True, nullable=False)
    passcode = Column(TEXT, nullable=False)

    def __init__(self, username: str, uid: int, passcode: str) -> None:
        super().__init__(uid, passcode)
        self.email = f'{username}@{Teacher.domain}'


if __name__ == '__main__':
    Base.metadata.create_all(engine, checkfirst=True)
    Student('kevin.nadar', 221078, 'kxn_2004')
    Student('ajay.nadar', 221077, 'akn_2004')
    print('Done!')
