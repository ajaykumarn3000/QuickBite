# -*- coding: utf-8 -*-
import os
from bcrypt import hashpw, gensalt, checkpw, hashpw
from sqlalchemy import Column, Integer, String
from database import conn as database, Base


def staff_exists(email: str) -> bool:
    """Function which checks if the staff exists in the database"""
    return bool(database.query(Staff).filter_by(email=email).all())


def correct_passcode(email: str, passcode: str) -> bool:
    """Function which checks if passcode is correct for the given uid"""
    user_passcode = passcode.encode()  # Convert it into bytes for bcrypt.
    database_passcode = (
        database.query(  # Using the database connection session
            Staff
        )  # Query the staff table in the database
        .filter_by(email=email)  # Filter the staff table by their email
        .first()  # Find the first occurrence of the user
        .passcode.encode()  # Extract the passcode from the user id  # Encode the output string into a bytes
    )
    return checkpw(user_passcode, database_passcode)


class Staff(Base):
    """Table which represents all the possible items in the Inventory"""

    __tablename__ = "staff"
    # The uid is created by an auto incrementing database key
    uid = Column(Integer, primary_key=True, autoincrement=True)
    # The email address of the staff member
    email = Column(String, unique=True, nullable=False)
    # The password set by the staff member
    passcode = Column(String, nullable=False)

    def __init__(self, email: str, passcode: str) -> None:
        """Code to be executed when a new user is instantiated"""
        self.email = email
        self.passcode = hashpw(passcode.encode(), gensalt()).decode()

    def save(self) -> None:
        """Save the user to the database"""
        database.add(self)
        database.commit()


# Create all the tables defined in the schema if they don't already exist
if not database.query(Staff).filter_by(uid=1).all():  # Admin has uid equal to 0
    # Create an instance of an Admin
    admin = Staff(
        email=os.environ.get("ADMIN_MAIL"), passcode=os.environ.get("PASSWORD")
    )
    # Add the admin to the database
    admin.save()
