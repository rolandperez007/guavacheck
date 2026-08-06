from fastapi import Request
from fastapi.responses import JSONResponse

API_SECRET = "dev-secret-change-this"


async def auth_guard(request: Request, call_next):
    # allow health endpoints
    if request.url.path in [
        "/health",
        "/ready",
        "/status",
        "/docs",
        "/openapi.json",
        "/redoc",
    ]:
        return await call_next(request)

    api_key = request.headers.get("x-api-key")

    if api_key != API_SECRET:
        return JSONResponse(status_code=401, content={"error": "Unauthorized"})

    return await call_next(request)
