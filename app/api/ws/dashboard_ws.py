import asyncio
import json

from fastapi import APIRouter, WebSocket

from irongate.ai.metrics import get_user_metrics
from irongate.ai.redis_client import client

router = APIRouter()


@router.websocket("/ws/dashboard")
async def dashboard_socket(ws: WebSocket):
    await ws.accept()

    while True:
        keys = client.keys("irongate:rep:*")

        payload = []

        for key in keys[:30]:
            user_id = key.replace("irongate:rep:", "")
            payload.append(get_user_metrics(user_id))

        await ws.send_text(json.dumps(payload))

        await asyncio.sleep(2)
