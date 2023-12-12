from typing import TypeVar

from src.database.models.base.core import Base

EntryType = TypeVar('EntryType')
Model = TypeVar('Model', bound=Base)
