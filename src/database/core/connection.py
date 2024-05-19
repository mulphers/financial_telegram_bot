from sqlalchemy.ext.asyncio import (AsyncEngine, AsyncSession,
                                    async_sessionmaker, create_async_engine)

SessionFactoryType = async_sessionmaker[AsyncSession]


def create_as_engine(url: str) -> AsyncEngine:
    return create_async_engine(
        url=url,
        echo=True
    )


def create_as_session_factory(engine: AsyncEngine) -> SessionFactoryType:
    return async_sessionmaker(bind=engine)
