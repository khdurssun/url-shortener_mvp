from fastapi import FastAPI

app = FastAPI(title="URL Shortener")


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}