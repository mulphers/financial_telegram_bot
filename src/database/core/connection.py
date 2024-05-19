from sqlalchemy.ext.asyncio import (AsyncEngine, async_sessionmaker,
                                    create_async_engine)

from src.common.types import SessionFactoryType


def create_as_engine(url: str) -> AsyncEngine:
    return create_async_engine(
        url=url,
        echo=True
    )


def create_as_session_factory(engine: AsyncEngine) -> SessionFactoryType:
    return async_sessionmaker(bind=engine)
