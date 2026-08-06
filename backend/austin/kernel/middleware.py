from __future__ import annotations

import time
from typing import Any

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from ..logger import structured_log
from .context import build_request_context


class AustinContextMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Any) -> Any:
        trace_id = (
            request.headers.get("x-trace-id")
            or request.headers.get("traceparent")
            or None
        )
        correlation_id = request.headers.get("x-correlation-id") or None
        request.state.trace_id = trace_id
        request.state.correlation_id = correlation_id
        request.state.context = build_request_context(
            trace_id=trace_id,
            correlation_id=correlation_id,
            user_context={"id": request.headers.get("x-user-id")},
            engine_context={"path": request.url.path},
        )
        started_at = time.perf_counter()
        response = await call_next(request)
        duration_ms = round((time.perf_counter() - started_at) * 1000, 2)
        structured_log(
            message="request completed",
            correlation_id=request.state.correlation_id,
            trace_id=request.state.trace_id,
            engine="austin",
            duration_ms=duration_ms,
            outcome="ok",
            severity="info",
            service=request.app.title,
        )
        return response
