from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.core.settings import load_settings

async_engine = create_async_engine(
    url=load_settings().db.url,
    echo=True
)
async_session_maker = async_sessionmaker(
    bind=async_engine
)
