from database.models.short_url import ShortURL
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


async def add_short_url_to_database(
    short_url: str,
    long_url: str,
    session: AsyncSession
):
    new_short_url = ShortURL(
        short_url=short_url,
        long_url=long_url,
    )
    session.add(new_short_url)
    await session.commit()
    await session.refresh(new_short_url)


async def get_long_url_and_increment_visits(
    short_url: str,
    session: AsyncSession,
) -> str | None:
    result = await session.execute(
        select(ShortURL).where(ShortURL.short_url == short_url)
    )
    url_entry = result.scalar_one_or_none()
    if not url_entry:
        return None
    url_entry.visits += 1
    await session.commit()
    return url_entry.long_url


async def get_visits_for_url(
    short_url: str,
    session: AsyncSession,
):
    result = await session.execute(
        select(ShortURL.visits).where(ShortURL.short_url == short_url)
    )
    visits = result.scalar_one_or_none()
    return visits


async def is_short_url_exist(short_url: str, session: AsyncSession) -> bool:
    result = await session.execute(
        select(ShortURL).where(ShortURL.short_url == short_url)
    )
    return result.scalar_one_or_none() is not None
