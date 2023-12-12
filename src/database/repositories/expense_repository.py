from datetime import date
from typing import Optional, Sequence, Type

from src.common.dto.expense import ExpanseCreate
from src.database.models.expense import Expense
from src.database.repositories.sqlalchemy_repository import \
    SQLAlchemyRepository


class ExpenseRepository(SQLAlchemyRepository[Expense]):
    model: Type[Expense] = Expense

    async def create_expense(self, data: ExpanseCreate) -> Optional[Expense]:
        return await self.create(data=data.model_dump())

    async def get_expense_for_day(self, user_id: int) -> Sequence[Expense]:
        today = date.today()

        return await self.get_many(
            self.model.user_id.__eq__(user_id),
            self.model.created_at.like(f'{today.year}-{today.month}-{today.day}%')
        )

    async def get_expense_for_month(self, user_id: int) -> Sequence[Expense]:
        today = date.today()

        return await self.get_many(
            self.model.user_id.__eq__(user_id),
            self.model.created_at.like(f'{today.year}-{today.month}-%')
        )

    async def get_expense_for_year(self, user_id: int) -> Sequence[Expense]:
        return await self.get_many(
            self.model.user_id.__eq__(user_id),
            self.model.created_at.like(f'{date.today().year}-%-%')
        )
