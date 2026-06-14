from fastapi import WebSocket


class WebSocketManager:
    def __init__(self):
        self.connections = []

    def connect(self, websocket: WebSocket):
        self.connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        if websocket in self.connections:
            self.connections.remove(websocket)

    async def broadcast(self, event: dict):
        dead_connections = []

        for ws in self.connections:
            try:
                await ws.send_json(event)
            except Exception:
                dead_connections.append(ws)

        for ws in dead_connections:
            self.connections.remove(ws)


# Shared global websocket manager
ws_manager = WebSocketManager()
