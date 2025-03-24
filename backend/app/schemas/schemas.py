from pydantic import BaseModel

class TransactionBase(BaseModel):
    type: str
    amount: float
    category: str
    description: str

class TransactionCreate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    id: int

    class Config:
        orm_mode = True