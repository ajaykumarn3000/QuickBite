import os
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from dotenv import load_dotenv

load_dotenv()


def create_connection():
    # Get DB Details from the environment variables
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = int(os.getenv("DB_PORT"))
    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")
    DB_NAME = os.getenv("DB_NAME")

    # Establish a connection to the PostgreSQL database
    db = QSqlDatabase.addDatabase("QPSQL")
    db.setHostName(DB_HOST)
    db.setPort(DB_PORT)
    db.setUserName(DB_USER)
    db.setPassword(DB_PASS)
    db.setDatabaseName(DB_NAME)
    if not db.open():
        print("Unable to open the database")
        return False
    return True


# Create connection to the database
create_connection()

# Create a QSqlTableModel object
orders_model = QSqlTableModel()

# Set the table name for the model
orders_model.setTable("orders")

# Load the data from the database
orders_model.select()
