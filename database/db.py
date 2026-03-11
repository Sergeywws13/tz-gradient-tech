from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from utils.config import load_config
from typing import AsyncIterator


config = load_config()


engine = create_async_engine(
    config.db.database_url,
    echo=config.db.echo
)


async_session = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def get_session() -> AsyncIterator[AsyncSession]:
    async with async_session() as session:
        yield session