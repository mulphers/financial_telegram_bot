from src.common.dto.expense import ExpanseCreate
from src.database.models.expense import Expense
from src.database.repositories.sqlalchemy_repository import \
    SQLAlchemyRepository


class ExpenseRepository(SQLAlchemyRepository):
    model = Expense

    async def create_expense(self, data: ExpanseCreate):
        return await self.create(data=data.model_dump())

    async def get_list_expense(self, user_id: int):
        return await self.get_many(
            field=self.model.user_id,
            value=user_id
        )
