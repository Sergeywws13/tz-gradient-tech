from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession

from database.crud import get_long_url_and_increment_visits, get_visits_for_url
from database.db import engine, get_session
from database.models.base import Base

from fastapi import Body, Depends, FastAPI
from fastapi import HTTPException
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from services.shortener import generate_short_url


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory='static'), name='static')


@app.get("/")
async def read_root():
    return FileResponse("static/index.html")


@app.post("/shorten")
async def generate_short_url_post(
    long_url: str = Body(embed=True),
    session: AsyncSession = Depends(get_session)
):
    new_short_url = await generate_short_url(long_url, session)
    return {"data": new_short_url}


@app.get("/{short_url}")
async def redirect_to_long_url(
    short_url: str,
    session: AsyncSession = Depends(get_session)
):
    long_url = await get_long_url_and_increment_visits(short_url, session)
    if not long_url:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return RedirectResponse(url=long_url)


@app.get("/stats/{short_url}")
async def get_stats_url(
    short_url: str,
    session: AsyncSession = Depends(get_session)
):
    visits = await get_visits_for_url(short_url, session)
    if visits is None:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return {"short_url": short_url, "visits": visits}
