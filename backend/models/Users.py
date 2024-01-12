# -*- coding: utf-8 -*-
from bcrypt import gensalt, hashpw
from sqlalchemy import create_engine, Column, INTEGER, TEXT
from sqlalchemy.orm import declarative_base, sessionmaker
from backend.logs.logger import logger

# The path to the database file
PATH_TO_DB = '../backend/database/database.sqlite'
# The domain name of the institution
DOMAIN = 'sfit.ac.in'

# Create connections to the database
Base = declarative_base()
engine = create_engine(f'sqlite:///{PATH_TO_DB}', echo='debug')
Session = sessionmaker(bind=engine)
session = Session()


class User:
    """A generalised user which shouldn't be instantiated directly."""

    def __init__(self, uid: int, passcode: str) -> None:
        # Initialise the unique identity of the user
        self.uid = uid
        # Initialise the passcode of the user
        self.passcode = passcode


class Student(User, Base):
    """A specialised user with a low priority."""

    # The table name in the database
    __tablename__ = 'student'
    # The domain of a student email address
    domain = f'{__tablename__}.{DOMAIN}'
    # Create the attributes of the student table
    uid = Column(INTEGER, primary_key=True)
    email = Column(TEXT, unique=True, nullable=False)
    passcode = Column(TEXT, nullable=False)

    def __init__(self, username: str, uid: int, passcode: str) -> None:
        # Hash the password before storing into the database
        hashed_password = hashpw(passcode.encode(), gensalt()).decode()
        # Specialise a user into a student
        super().__init__(uid, hashed_password)
        # Formulate the email address of the student
        self.email = f'{username}@{Student.domain}'
        # Log the creation of a new student
        logger.info(f'Created a student with pid {self.uid}')

    def add_student(self) -> None:
        """Add the student to the database"""

        session.add(self)
        session.commit()
        # Log the addition of the new student
        logger.info(f'Added a student with pid {self.uid}')


class Teacher(User, Base):
    """A specialised user with a high priority."""

    # The table name in the database
    __tablename__ = 'teacher'
    # NOTE: No need for teacher's domain, same as college
    # Create the attributes of the teacher's table
    uid = Column(INTEGER, primary_key=True)
    email = Column(TEXT, unique=True, nullable=False)
    passcode = Column(TEXT, nullable=False)

    def __init__(self, username: str, uid: int, passcode: str) -> None:
        # Hash the password before storing into the database
        hashed_password = hashpw(passcode.encode(), gensalt()).decode()
        # Specialise a user into a teacher
        super().__init__(uid, hashed_password)
        # Formulate the email address of the teacher
        self.email = f'{username}@{DOMAIN}'
        # Log the creation of a new teacher
        logger.info(f'Created a teacher with uid {self.uid}')

    def add_teacher(self) -> None:
        """Add a teacher to the database"""

        session.add(self)
        session.commit()
        # Log the addition of the new teacher
        logger.info(f'Added teacher with uid {self.uid}')


# Create the database/table if not exists, else skip
Base.metadata.create_all(engine, checkfirst=True)
