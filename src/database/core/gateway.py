from __future__ import annotations

from types import TracebackType
from typing import AsyncGenerator, Optional, Type

from src.common.interfaces.abstract_uow import AbstractUnitOfWork
from src.common.types import SessionFactoryType
from src.database.core.sqlalchemy_uow import sqlalchemy_unit_of_work_factory
from src.database.repositories.expense_repository import ExpenseRepository
from src.database.repositories.user_repository import UserRepository


class DatabaseGateway:
    def __init__(self, uow: AbstractUnitOfWork) -> None:
        self.uow = uow

    async def __aenter__(self) -> DatabaseGateway:
        await self.uow.__aenter__()
        return self

    async def __aexit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optional[TracebackType]
    ) -> None:
        await self.uow.__aexit__(exc_type, exc_val, exc_tb)

    def user_repository(self) -> UserRepository:
        return UserRepository(self.uow.session)

    def expense_repository(self) -> ExpenseRepository:
        return ExpenseRepository(self.uow.session)


class TransactionGateway:
    def __init__(self, session_factory: SessionFactoryType) -> None:
        self.session_factory = session_factory

    async def __call__(self) -> AsyncGenerator[DatabaseGateway, None]:
        async with database_gateway_factory(
                uow=sqlalchemy_unit_of_work_factory(session=self.session_factory())
        ) as gateway:
            yield gateway


def database_gateway_factory(uow: AbstractUnitOfWork) -> DatabaseGateway:
    return DatabaseGateway(uow=uow)
