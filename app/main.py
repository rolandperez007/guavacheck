# app/main.py
from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI

from app.api.routes.austin import router as austin_router

app = FastAPI(
    title="Austin Engine",
    version="0.1.0"
)

app.include_router(austin_router, prefix="/austin", tags=["Austin"])

@app.get("/")
async def health():
    return {
        "status": "Austin API running"
    }
    from app.api.austin import router as austin_router

app.include_router(
    austin_router,
    prefix="/api/austin",
    tags=["Austin"]
)