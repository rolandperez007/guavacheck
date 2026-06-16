from fastapi import Request
from fastapi.responses import JSONResponse

API_SECRET = "dev-secret-change-this"


async def auth_guard(request: Request, call_next):
    # allow public routes
    if request.url.path in ["/health", "/ready", "/status", "/docs", "/openapi.json"]:
        return await call_next(request)

    # check API key
    auth = request.headers.get("x-api-key")

    if auth != API_SECRET:
        return JSONResponse(
            status_code=401,
            content={"error": "Unauthorized - missing or invalid API key"}
        )

    # IMPORTANT: allow request to continue
    return await call_next(request)