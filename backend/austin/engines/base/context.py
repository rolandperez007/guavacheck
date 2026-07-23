"""
Austin Engine Context

Shared execution context passed into every engine.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class EngineContext:

    session_id: str

    correlation_id: str

    trace_id: str

    message: str

    history: list[dict] = field(default_factory=list)

    summary: str = ""

    world: dict[str, Any] = field(default_factory=dict)

    metadata: dict[str, Any] = field(default_factory=dict)