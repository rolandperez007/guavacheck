from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4


@dataclass
class RequestContext:
    trace_id: str
    correlation_id: str
    user_context: dict[str, Any] = field(default_factory=dict)
    engine_context: dict[str, Any] = field(default_factory=dict)
    request_started_at: str | None = None


def build_request_context(
    *,
    trace_id: str | None = None,
    correlation_id: str | None = None,
    user_context: dict[str, Any] | None = None,
    engine_context: dict[str, Any] | None = None,
) -> RequestContext:
    return RequestContext(
        trace_id=trace_id or str(uuid4()),
        correlation_id=correlation_id or str(uuid4()),
        user_context=user_context or {},
        engine_context=engine_context or {},
    )
