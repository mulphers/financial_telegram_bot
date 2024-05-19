from sqlalchemy.ext.asyncio import AsyncSession, AsyncSessionTransaction

from src.common.interfaces.abstract_uow import AbstractUnitOfWork


class SQLAlchemyUnitOfWork(AbstractUnitOfWork[AsyncSession, AsyncSessionTransaction]):
    async def commit(self) -> None:
        await self.session.commit()

    async def rollback(self) -> None:
        await self.session.rollback()

    async def create_transaction(self) -> None:
        if not self.session.in_transaction() and self.session.is_active:
            self.transaction = await self.session.begin()

    async def close_transaction(self) -> None:
        if self.session.is_active:
            await self.session.close()


def sqlalchemy_unit_of_work_factory(session: AsyncSession) -> SQLAlchemyUnitOfWork:
    return SQLAlchemyUnitOfWork(session=session)
