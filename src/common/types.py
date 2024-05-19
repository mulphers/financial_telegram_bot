from typing import TypeVar

from src.database.models.base.core import Base

ModelType = TypeVar('ModelType', bound=Base)

SessionType = TypeVar('SessionType')
TransactionType = TypeVar('TransactionType')

EntryType = TypeVar('EntryType')
ColumnType = TypeVar('ColumnType')
