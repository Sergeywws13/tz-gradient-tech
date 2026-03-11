import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from database.crud import (
    add_short_url_to_database,
    get_long_url_and_increment_visits,
    get_visits_for_url,
    is_short_url_exist,
)
from database.models.short_url import ShortURL


pytestmark = pytest.mark.asyncio


async def test_add_short_url_to_database(session: AsyncSession):
    """
    Проверяет, что функция корректно добавляет запись в БД.

    Убеждается, что поле visits устанавливается в 0 по умолчанию.
    """
    short = "abc123"
    long_url = "https://example.com"
    await add_short_url_to_database(short, long_url, session)
    # Проверяем, что запись появилась
    result = await session.get(ShortURL, short)
    assert result is not None
    assert result.long_url == long_url
    assert result.visits == 0


async def test_is_short_url_exist(session: AsyncSession):
    """
    Проверяет, что функция правильно определяет существование короткого URL.

    Сначала возвращает False для несуществующего, после добавления – True.
    """
    short = "exist123"
    assert not await is_short_url_exist(short, session)
    # Добавляем
    await add_short_url_to_database(short, "https://example.com", session)
    assert await is_short_url_exist(short, session)


async def test_get_long_url_and_increment_visits(session: AsyncSession):
    """
    Проверяет, что при первом вызове возвращается длинный URL, а счётчик visits увеличивается с 0 до 1.

    При повторном вызове счётчик снова увеличивается (до 2).

    Гарантирует, что инкремент работает корректно и данные сохраняются.
    """
    short = "inc123"
    long_url = "https://example.com"
    await add_short_url_to_database(short, long_url, session)

    # Первый переход
    retrieved = await get_long_url_and_increment_visits(short, session)
    assert retrieved == long_url

    # Проверяем visits
    result = await session.get(ShortURL, short)
    assert result.visits == 1

    # Второй переход
    retrieved = await get_long_url_and_increment_visits(short, session)
    assert retrieved == long_url
    await session.refresh(result)
    assert result.visits == 2


async def test_get_visits_for_url(session: AsyncSession):
    """
    Проверяет, что функция возвращает текущее количество переходов.

    Для новой записи возвращает 0, после перехода – 1.

    Для несуществующей ссылки возвращает None.
    """
    short = "stats123"
    long_url = "https://example.com"
    await add_short_url_to_database(short, long_url, session)

    visits = await get_visits_for_url(short, session)
    assert visits == 0

    # Увеличим через функцию
    await get_long_url_and_increment_visits(short, session)
    visits = await get_visits_for_url(short, session)
    assert visits == 1

    # Несуществующий URL
    visits = await get_visits_for_url("nonexist", session)
    assert visits is None
