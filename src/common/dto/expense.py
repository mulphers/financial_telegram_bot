from pydantic import BaseModel


class ExpanseCreate(BaseModel):
    user_id: int
    amount_expense: float
    short_description: str
