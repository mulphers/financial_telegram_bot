from functools import wraps
from typing import Any, Callable

from src.database.core.sqlalchemy_uow import SQLAlchemyUnitOfWork


def with_database(handler: Callable) -> Callable:
    @wraps(handler)
    async def wrapper(*args: Any, **kwargs: Any) -> Any:
        async with SQLAlchemyUnitOfWork() as uow:
            kwargs['uow'] = uow
            return await handler(*args, **kwargs)

    return wrapper
