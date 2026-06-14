from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.middleware.irongate_middleware import irongate_guard
from app.api.routes.austin import router as austin_router
from app.api.ws.austin_ws import router as ws_router
from app.core.health import router as health_router
from app.api.routes.irongate import router as irongate_router
from app.api.routes.dashboard import router as dashboard_router
from app.api.ws.dashboard_ws import router as dashboard_ws
from app.api.routes.irongate_dashboard import router as irongate_dashboard_router
from app.api.routes.irongate_control import router as control_router

app.include_router(control_router)
from fastapi import WebSocket
import asyncio
from irongate.telemetry import get_recent


@router.websocket("/control/live")
async def live(ws: WebSocket):
    await ws.accept()

    last_count = 0

    while True:
        data = get_recent()

        if len(data) != last_count:
            await ws.send_json({"type": "update", "events": data})
            last_count = len(data)

        await asyncio.sleep(1)


app.include_router(irongate_dashboard_router)

app = FastAPI(title="Austin V3")

# ✅ FUNCTION MIDDLEWARE (correct way)
app.middleware("http")(irongate_guard)

# routes
app.include_router(austin_router, prefix="/austin")
app.include_router(irongate_router)
app.include_router(ws_router)
app.include_router(health_router)
app.include_router(dashboard_router)
app.include_router(dashboard_ws)

# static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# debug
print("WS ROUTES:")
for r in app.routes:
    print(r)
