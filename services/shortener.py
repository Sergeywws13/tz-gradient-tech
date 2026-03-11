from urllib.parse import urlparse
from services.generate_short_url import generate_random_url
from database.crud import add_short_url_to_database
from sqlalchemy.ext.asyncio import AsyncSession
from database.crud import is_short_url_exist


async def generate_short_url(long_url: str, session: AsyncSession) -> str:
    if not urlparse(long_url).scheme:
        long_url = "https://" + long_url

    while True:
        short_url = generate_random_url()
        if not await is_short_url_exist(short_url, session):
            break

    await add_short_url_to_database(
        short_url, long_url, session
    )
    return short_url
