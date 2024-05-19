from typing import TypeVar

from src.database.models.base.core import Base

ModelType = TypeVar('ModelType', bound=Base)

SessionType = TypeVar('SessionType')

EntryType = TypeVar('EntryType')
ColumnType = TypeVar('ColumnType')
