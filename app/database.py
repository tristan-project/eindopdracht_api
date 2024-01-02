#libqries ophalen
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#connecteren met de database
import os

# Read the DATABASE_URL environment variable

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./sqlitedb/sqlitedata1.db")
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlitedb/sqlitedata1.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

#qqnmqken
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



# gebruikt in main.py
Base = declarative_base()