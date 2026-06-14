from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.core.austin_engine import AustinEngine
from app.core.security.context import SecurityContext
import traceback

router = APIRouter()
engine = AustinEngine()


@router.websocket("/ws/austin")
async def austin_socket(websocket: WebSocket):
    await websocket.accept()

    await websocket.send_json(
        {"type": "system", "status": "connected", "message": "Austin WebSocket active"}
    )

    try:
        while True:
            query = await websocket.receive_text()

            if not query or not query.strip():
                await websocket.send_json(
                    {"type": "error", "message": "Empty query received"}
                )
                continue

            context = SecurityContext(user_id="test-user", org_id="test-org")

            try:
                async for chunk in engine.stream_execute(query, context):
                    await websocket.send_json({"type": "chunk", "data": chunk})

                await websocket.send_json({"type": "done"})

            except Exception as e:
                await websocket.send_json({"type": "error", "message": str(e)})
                traceback.print_exc()

    except WebSocketDisconnect:
        print("Austin client disconnected")

    except Exception as e:
        print("WebSocket fatal error:", e)
        traceback.print_exc()
