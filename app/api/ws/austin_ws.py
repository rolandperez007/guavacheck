import json
from fastapi import WebSocket, APIRouter

from app.core.austin_parser import AustinParser
from app.core.austin_brain import AustinBrain
from app.core.austin_gpt_brain import AustinGPTBrain
from app.services.ai_ratings import get_system_snapshot
from app.core.austin_memory import AustinMemory

router = APIRouter()

parser = AustinParser()
brain = AustinBrain()
gpt = AustinGPTBrain()
memory = AustinMemory()

@router.websocket("/ws/austin")
async def austin_socket(websocket: WebSocket):
    await websocket.accept()

    while True:
        raw = await websocket.receive_text()

        try:
            data = json.loads(raw)
        except Exception:
            data = {"query": raw, "user_id": "unknown"}

        query = data.get("query", "")

        # -----------------------------
        # 1. THINKING
        # -----------------------------
        await websocket.send_json({
            "type": "chunk",
            "data": {
                "type": "thinking",
                "stage": "start",
                "message": "Analyzing request..."
            }
        })

        # -----------------------------
        # 2. PARSE INPUT
        # -----------------------------
        parsed = parser.parse(query)

        # -----------------------------
        # 3. BRAIN ANALYSIS
        # -----------------------------
        analysis = brain.analyze(parsed)

        # -----------------------------
        # 4. GPT EXPLANATION
        # -----------------------------
        explanation = gpt.reason(query, analysis)

        # -----------------------------
        # 5. DASHBOARD EVENT
        # -----------------------------
        event = {
            "query": query,
            "analysis": analysis,
            "decision": analysis.get("decision"),
            "score": analysis.get("score")
        }

        snapshot = get_system_snapshot()
        snapshot["last_austin_event"] = event

        # -----------------------------
        # 6. SEND CONTEXT (optional)
        # -----------------------------
        await websocket.send_json({
            "type": "chunk",
            "data": {
                "type": "context",
                "data": {
                    "query": query,
                    "history": history[-5:],  # last 5 interactions
                    "status": "processed"
                }
            }
       })

        # -----------------------------
        # 7. SEND ANALYSIS
        # -----------------------------
        await websocket.send_json({
            "type": "chunk",
            "data": {
                "type": "analysis",
                "data": analysis
            }
        })

        # -----------------------------
        # 8. SEND RESPONSE (GPT)
        # -----------------------------
        await websocket.send_json({
            "type": "chunk",
            "data": {
                "type": "response",
                "message": explanation
            }
        })

        # -----------------------------
        # 9. DASHBOARD EVENT STREAM
        # -----------------------------
        await websocket.send_json({
            "type": "chunk",
            "data": {
                "type": "dashboard_event",
                "data": event
            }
        })
        memory.save(user_id, event)
        history = memory.get_history(user_id)
        
        # -----------------------------
        # 10. DONE
        # -----------------------------
        await websocket.send_json({
            "type": "done"
        })