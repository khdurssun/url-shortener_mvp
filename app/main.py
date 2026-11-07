from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_session

app = FastAPI(title="URL Shortener")


@app.get("/health")
async def health_check(
    session: AsyncSession = Depends(get_session),
) -> dict[str, str]:
    await session.execute(text("SELECT 1"))

    return {"status": "ok"}