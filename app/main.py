# app/main.py

from fastapi import FastAPI

from app.api.routes.austin import router as austin_router

app = FastAPI(
    title="Austin Engine",
    version="0.1.0"
)

app.include_router(austin_router)

@app.get("/")
async def health():
    return {
        "status": "Austin API running"
    }