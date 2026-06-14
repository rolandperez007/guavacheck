from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from app.core.realtime.websocket_manager import ws_manager

app = FastAPI()
manager = ws_manager


@app.websocket("/ws/austin")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    manager.connect(websocket)

    try:
        while True:
            # keep connection alive
            data = await websocket.receive_text()

            # optional echo (debug only)
            await manager.broadcast({"event": "client.message", "payload": data})

    except WebSocketDisconnect:
        manager.disconnect(websocket)
