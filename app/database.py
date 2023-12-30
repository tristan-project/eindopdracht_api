#libqries ophalen
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#connecteren met de database
SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlitedb/sqlitedata1.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

#qqnmqken
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



# gebruikt in main.py
Base = declarative_base()