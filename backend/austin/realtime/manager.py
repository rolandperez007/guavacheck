"""
Austin Realtime Connection Manager

Maintains all active websocket connections for the
Engineering Command Center.
"""

from __future__ import annotations

from typing import Any

from fastapi import WebSocket


class RealtimeManager:
    """
    Tracks all connected dashboard clients.
    """

    def __init__(self) -> None:
        self.connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket) -> None:
        """
        Accept a websocket connection.
        """
        await websocket.accept()

        if websocket not in self.connections:
            self.connections.append(websocket)

    def disconnect(self, websocket: WebSocket) -> None:
        """
        Remove a websocket connection.
        """
        if websocket in self.connections:
            self.connections.remove(websocket)

    async def broadcast(self, payload: dict[str, Any]) -> None:
        """
        Send an event to every connected client.
        """

        dead_connections: list[WebSocket] = []

        for websocket in self.connections:
            try:
                await websocket.send_json(payload)
            except Exception:
                dead_connections.append(websocket)

        for websocket in dead_connections:
            self.disconnect(websocket)

    @property
    def connection_count(self) -> int:
        return len(self.connections)


realtime_manager = RealtimeManager()
