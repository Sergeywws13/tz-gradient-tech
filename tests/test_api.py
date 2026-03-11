import pytest
from httpx import AsyncClient

pytestmark = pytest.mark.asyncio


async def test_create_short_url(client: AsyncClient):
    response = await client.post("/shorten", json={"long_url": "https://example.com"})
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    short_url = data["data"]
    assert len(short_url) == 6


async def test_create_short_url_normalizes(client: AsyncClient):
    # Проверяем, что google.com превращается в https://google.com
    response = await client.post("/shorten", json={"long_url": "google.com"})
    assert response.status_code == 200
    short_url = response.json()["data"]
    
    # Сделаем GET и проверим Location
    resp = await client.get(f"/{short_url}", follow_redirects=False)
    assert resp.status_code == 307
    assert resp.headers["location"] == "https://google.com"


async def test_redirect_and_visits(client: AsyncClient):
    create_resp = await client.post("/shorten", json={"long_url": "https://python.org"})
    short = create_resp.json()["data"]

    # Первый переход
    resp1 = await client.get(f"/{short}", follow_redirects=False)
    assert resp1.status_code == 307
    assert resp1.headers["location"] == "https://python.org"

    # Проверяем статистику
    stats_resp = await client.get(f"/stats/{short}")
    assert stats_resp.status_code == 200
    assert stats_resp.json()["visits"] == 1

    # Второй переход
    resp2 = await client.get(f"/{short}", follow_redirects=False)
    assert resp2.status_code == 307

    # Обновляем статистику
    stats_resp2 = await client.get(f"/stats/{short}")
    assert stats_resp2.status_code == 200
    assert stats_resp2.json()["visits"] == 2


async def test_nonexistent_short_url(client: AsyncClient):
    resp = await client.get("/nonexist", follow_redirects=False)
    assert resp.status_code == 404

    stats_resp = await client.get("/stats/nonexist")
    assert stats_resp.status_code == 404


async def test_stats_endpoint(client: AsyncClient):
    # Создаём ссылку
    create_resp = await client.post("/shorten", json={"long_url": "https://fastapi.tiangolo.com"})
    short = create_resp.json()["data"]

    # Статистика до переходов
    stats = await client.get(f"/stats/{short}")
    assert stats.json()["visits"] == 0

    # Делаем переход
    await client.get(f"/{short}", follow_redirects=False)

    # Проверяем статистику
    stats = await client.get(f"/stats/{short}")
    assert stats.json()["visits"] == 1
