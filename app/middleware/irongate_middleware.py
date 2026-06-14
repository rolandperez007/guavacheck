from fastapi import Request
from fastapi.responses import JSONResponse
from irongate.bootstrap import gate
from irongate.normalizer import normalize_request
from irongate import audit


async def irongate_guard(request: Request, call_next):
    try:
        body = await request.json()
    except Exception:
        body = {}

    context = normalize_request(request, body)

    context["auth_header"] = request.headers.get("authorization")
    context["api_key"] = request.headers.get("x-api-key")

    decision = gate.evaluate(context)

    try:
        audit.log_event(context, decision)
    except Exception:
        pass

    if isinstance(decision, dict):
        if not decision.get("allowed", True):
            return JSONResponse(status_code=403, content=decision)
        return await call_next(request)

    if isinstance(decision, str):
        return JSONResponse(status_code=403, content={"reason": decision})

    if decision is False:
        return JSONResponse(status_code=403, content={"reason": "blocked"})

    return await call_next(request)
