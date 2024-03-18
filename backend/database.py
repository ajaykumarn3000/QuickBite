import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()  # Load all the environment variables

DB_CONNECTION_STRING = os.environ["DB_CONNECTION_STRING"]

engine = create_engine(DB_CONNECTION_STRING)

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

conn = SessionLocal()

Base.metadata.create_all(bind=engine, checkfirst=True)
