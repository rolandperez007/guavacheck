"""
Austin WebSocket Routes
"""

from __future__ import annotations

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from backend.austin.realtime import realtime_manager

router = APIRouter(
    prefix="/austin/ws",
    tags=["Austin WebSocket"],
)


@router.websocket("/events")
async def websocket_events(websocket: WebSocket):

    await realtime_manager.connect(websocket)

    try:
        while True:
            # Keep the connection alive.
            await websocket.receive_text()

    except WebSocketDisconnect:
        realtime_manager.disconnect(websocket)