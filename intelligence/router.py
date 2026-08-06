from fastapi import APIRouter

from .collector import collector
from .schemas import IntelligenceEvent
from .service import service

router = APIRouter(
    prefix="/intelligence",
    tags=["Guava Intelligence"],
)


@router.post("/event")
async def collect_event(payload: IntelligenceEvent):

    event = await collector.collect(payload)

    return await service.store(event)
