from typing import TypeVar

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.database.models.base.core import Base

ModelType = TypeVar('ModelType', bound=Base)

SessionType = TypeVar('SessionType')
TransactionType = TypeVar('TransactionType')

EntryType = TypeVar('EntryType')
ColumnType = TypeVar('ColumnType')

SessionFactoryType = async_sessionmaker[AsyncSession]
