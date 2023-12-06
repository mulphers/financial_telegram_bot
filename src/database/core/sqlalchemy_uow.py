from src.common.interfaces.abstract_uow import AbstractUnitOfWork


class SQLAlchemyUnitOfWork(AbstractUnitOfWork):
    async def commit(self) -> None:
        await self.session.commit()

    async def rollback(self) -> None:
        await self.session.rollback()
