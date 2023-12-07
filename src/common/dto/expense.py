from pydantic import BaseModel


class ExpenseDTO(BaseModel):
    expense_id: int
    user_id: int
    amount_expense: float
    short_description: str


class ExpanseCreate(BaseModel):
    user_id: int
    amount_expense: float
    short_description: str
