from __future__ import annotations

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter(prefix="/ws", tags=["WebSocket"])


class ConnectionManager:
    def __init__(self) -> None:
        self._connections: set[WebSocket] = set()

    async def connect(self, websocket: WebSocket) -> None:
        await websocket.accept()
        self._connections.add(websocket)

    def disconnect(self, websocket: WebSocket) -> None:
        self._connections.discard(websocket)

    async def broadcast(self, message: dict) -> None:
        for connection in list(self._connections):
            try:
                await connection.send_json(message)
            except Exception:
                self.disconnect(connection)


manager = ConnectionManager()


@router.websocket("/austin")
async def austin_socket(websocket: WebSocket) -> None:
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)
