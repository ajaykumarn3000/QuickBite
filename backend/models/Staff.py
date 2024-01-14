# -*- coding: utf-8 -*-
from os import environ
from bcrypt import hashpw, gensalt, checkpw, hashpw
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


def staff_exists(email: str) -> bool:
    """Function which checks if the staff exists in the database"""
    return bool(database.query(Staff).filter_by(email=email).all())


def correct_passcode(email: str, passcode: str) -> bool:
    """Function which checks if passcode is correct for the given uid"""
    user_passcode = passcode.encode()
    database_passcode = (database  # Using the database connection session
        .query(Staff)              # Query the staff table in the database
        .filter_by(email=email)    # Filter the staff table by their email
        .first()                   # Find the first occurrence of the user
        .passcode                  # Extract the passcode from the user id         # Encode the output string into a bytes
    )
    return checkpw(user_passcode, database_passcode)


class Staff(Base):
    """Table which represents all the possible items in the Inventory"""
    __tablename__ = 'staff'
    # The uid is created by an auto incrementing database key
    uid = Column(INTEGER, primary_key=True, autoincrement=True)
    # The email address of the staff member
    email = Column(TEXT, unique=True, nullable=False)
    # The password set by the staff member
    passcode = Column(TEXT, nullable=False)

    def __init__(self, email: str, passcode: str) -> None:
        """Code to be executed when a new user is instantiated"""
        self.email = email
        self.passcode = hashpw(passcode.encode(), gensalt())

    def save(self) -> None:
        """Save the user to the database"""
        database.add(self)
        database.commit()


# Create all the tables defined in the schema if they don't already exist
Base.metadata.create_all(engine)

# If the Admin doesn't exist in the staff table
if not database.query(Staff).filter_by(uid=0).all():  # Admin has uid equal to 0
    # Create an instance of an Admin
    admin = Staff(email=environ.get('ADMIN_MAIL'), passcode=environ.get('PASSWORD'))
    # Add the admin to the database
    admin.save()
