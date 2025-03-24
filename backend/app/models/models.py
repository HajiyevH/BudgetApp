from sqlalchemy import Column, Integer, String, Float
from app.database.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(10), index=True)  # "income" or "expense"
    amount = Column(Float)
    category = Column(String(50))
    description = Column(String(255))