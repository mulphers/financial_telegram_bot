from __future__ import annotations

from abc import ABC, abstractmethod

from src.database.core.connection import async_session_maker
from src.database.repositories.expense_repository import ExpenseRepository
from src.database.repositories.user_repository import UserRepository


class AbstractUnitOfWork(ABC):
    def __init__(self) -> None:
        self.session_factory = async_session_maker

    async def __aenter__(self) -> AbstractUnitOfWork:
        print('-' * 30)
        print('__aenter__')
        print('-' * 30)

        self.session = self.session_factory()

        # Register your repositories here
        # self.<name_repo> = <class_repo>(self.session)
        self.user = UserRepository(self.session)
        self.expense = ExpenseRepository(self.session)

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type:
            await self.rollback()
        else:
            await self.commit()

        await self.session.close()

        print('-' * 30)
        print('__aexit__')
        print('-' * 30)

    @abstractmethod
    async def commit(self) -> None:
        pass

    @abstractmethod
    async def rollback(self) -> None:
        pass
