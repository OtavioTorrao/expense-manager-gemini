from pydantic import BaseModel
from datetime import datetime
from typing import Union

class ExpenseBase(BaseModel):
    title: str
    amount: float
    description: Union[str, None] = None
    category: Union[str, None] = "outros"

class ExpenseCreate(ExpenseBase):
    pass

class Expense(ExpenseBase):
    id: int
    created_at: datetime
    updated_at: Union[datetime, None] = None

    class Config:
        orm_mode = True
