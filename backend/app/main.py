from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import SessionLocal, engine, Base
from app.models.models import Transaction
from app.schemas.schemas import TransactionCreate, TransactionResponse
from typing import List

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Add a Transaction (POST)
@app.post("/add_transaction/", response_model=TransactionResponse)
def add_transaction(transaction_data: TransactionCreate, db: Session = Depends(get_db)):
    db_transaction = Transaction(**transaction_data.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

# Get All Transactions (GET)
@app.get("/transactions/", response_model=List[TransactionResponse])
def get_transactions(db: Session = Depends(get_db)):
    return db.query(Transaction).all()

# Get Account Balance
@app.get("/balance/")
def get_balance(db: Session = Depends(get_db)):
    balance = sum(
        t.amount if t.type == "income" else -t.amount for t in db.query(Transaction).all()
    )
    return {"balance": balance}