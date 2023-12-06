from functools import wraps
from typing import Callable

from src.database.core.sqlalchemy_uow import SQLAlchemyUnitOfWork


def with_database(handler: Callable):
    @wraps(handler)
    async def wrapper(*args, **kwargs):
        async with SQLAlchemyUnitOfWork() as uow:
            kwargs['uow'] = uow
            return await handler(*args, **kwargs)

    return wrapper
