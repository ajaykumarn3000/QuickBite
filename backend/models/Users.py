# -*- coding: utf-8 -*-
from pandas import read_excel
from bcrypt import gensalt, hashpw, checkpw
from sqlalchemy import Column, Integer, String
from database import conn as database, Base

# Path to the workbook containing the user data (uid, name, email)
WORKBOOK = "./data/Student List 2024.xls"
# Name of the spreadsheet containing the data
SPREADSHEET = "Student List SEITB"
# The domain name of the institution
DOMAIN = "sfit.ac.in"

student_data = read_excel(WORKBOOK, sheet_name=SPREADSHEET)


def get_name_by_email(email: str) -> str:
    """Function which returns the name"""
    name = student_data[student_data["Email"] == email]["Name"].values[0]
    name = name.split()[:2]
    name.reverse()
    return " ".join(name).title()


def find_id(email: str) -> list[int]:
    """Function which checks if the sfit email exists or not"""
    return student_data[student_data["Email"] == email]["PID"].values


def id_exists(uid: int) -> list:
    """Function which checks if the uid is registered or not"""
    return database.query(User).filter_by(uid=uid).all()


def user_exists(email: str) -> list:
    """Function which checks if sfit email already exists or not"""
    return database.query(User).filter_by(email=email).all()


def correct_passcode(uid: int, passcode: str) -> bool:
    """Function which checks if passcode is correct for the given uid"""
    user_passcode = passcode.encode()  # Convert it into bytes for bcrypt.
    database_passcode = (
        database.query(  # Using the database connection session
            User
        )  # Query the staff table in the database
        .filter_by(uid=uid)  # Filter the staff table by their email
        .first()  # Find the first occurrence of the user
        .passcode.encode()  # Extract the passcode from the user id  # Encode the output string into a bytes
    )
    return checkpw(user_passcode, database_passcode)


class User(Base):
    """Class to represent a user in the database"""

    # The name of the table in the database
    __tablename__ = "users"
    # The unique identifier of all users
    uid = Column(Integer, primary_key=True)
    # The name of the user
    name = Column(String, nullable=False)
    # The sfit affiliated email of the user
    email = Column(String, unique=True, nullable=False)
    # The passcode of choice on registering
    passcode = Column(String, nullable=False)

    def __init__(self, uid: str, email: str, passcode: str) -> None:
        """Code to be executed when a new user is instantiated"""
        self.uid = int(uid)
        self.name = get_name_by_email(email=email)
        self.email = email
        self.passcode = hashpw(passcode.encode("utf-8"), gensalt()).decode()

    def save(self) -> None:
        """Save the user to the database"""
        database.add(self)
        database.commit()
