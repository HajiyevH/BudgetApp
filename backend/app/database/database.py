from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite Database URL
DATABASE_URL = "sqlite:///./budget.db"

# Create Database Engine (connect_args allows multiple threads)
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base Class for ORM Models
Base = declarative_base()