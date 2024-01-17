# -*- coding: utf-8 -*-
from pandas import read_excel
from bcrypt import gensalt, hashpw, checkpw
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import create_engine, Column, INTEGER, TEXT

# Path to the workbook containing the user data (uid, name, email)
WORKBOOK = 'data/Student List 2024.xls'
# Name of the spreadsheet containing the data
SPREADSHEET = 'Student List SEITB'
# The path to the database file
DATABASE = 'database/database.db'
# The domain name of the institution
DOMAIN = 'sfit.ac.in'

student_data = read_excel(WORKBOOK, sheet_name=SPREADSHEET)

# Instantiate the ORM of the database to a python object
Base = declarative_base()
# Create a connection to a database using its file path
engine = create_engine(f'sqlite:///{DATABASE}')
# engine = create_engine('postgresql://quickbite_user:5R4sTQ8YoDIJgQJcAEqhKfQaLgCvL3rw@dpg-cmjr0inqd2ns73bkrr00-a.singapore-postgres.render.com/quickbite')
# A session to connect to the database connection
database = Session(bind=engine)


# TODO: Add name of user from excel workbook
def get_name_by_uid(uid: int) -> str:
    """Function which returns the name of the user"""
    return student_data[student_data['PID'] == uid]['Name'].values[0]


def get_name_by_email(email: str) -> str:
    """Function which returns the name"""
    name = student_data[student_data['Email'] == email]['Name'].values[0]
    name = name.split()[:2]
    name.reverse()
    return ' '.join(name).title()


def find_id(email: str) -> list[int]:
    """Function which checks if the sfit email exists or not"""
    return student_data[student_data['Email'] == email]['PID'].values


def id_exists(uid: int) -> list:
    """Function which checks if the uid is registered or not"""
    return database.query(User).filter_by(uid=uid).all()


def user_exists(email: str) -> list:
    """Function which checks if sfit email already exists or not"""
    return database.query(User).filter_by(email=email).all()


def correct_passcode(uid: int, passcode: str) -> bool:
    """Function which checks if passcode is correct for the given uid"""
    user_passcode = passcode.encode('utf-8')
    database_passcode = bytes(database.query(User).filter_by(uid=uid).first().passcode)
    print(user_passcode, database_passcode)
    return checkpw(user_passcode, database_passcode)


class User(Base):
    """Class to represent a user in the database"""
    # The name of the table in the database
    __tablename__ = 'users'
    # The unique identifier of all users
    uid = Column(INTEGER, primary_key=True)
    # The name of the user
    name = Column(TEXT, nullable=False)
    # The sfit affiliated email of the user
    email = Column(TEXT, unique=True, nullable=False)
    # The passcode of choice on registering
    passcode = Column(TEXT, nullable=False)

    def __init__(self, uid: str, email: str, passcode: str) -> None:
        """Code to be executed when a new user is instantiated"""
        self.uid = int(uid)
        self.name = get_name_by_uid(uid=int(uid))
        self.email = email
        self.passcode = hashpw(passcode.encode('utf-8'), gensalt())

    def save(self) -> None:
        """Save the user to the database"""
        database.add(self)
        database.commit()


# Create the database/table if not exists, else skip
Base.metadata.create_all(engine, checkfirst=True)
