"""
Austin Runtime Execution Context

Carries the complete execution state throughout Austin's runtime.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass(slots=True)
class ExecutionContext:
    """
    Complete runtime context supplied to every Austin engine.
    """

    session_id: str
    message: str

    history: list[dict[str, Any]] = field(default_factory=list)
    summary: str = ""

    world: dict[str, Any] = field(default_factory=dict)
    memory: list[dict[str, Any]] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    execution_plan: Any | None = None

    correlation_id: str = ""
    trace_id: str = ""

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    configuration: dict[str, Any] = field(default_factory=dict)

    runtime: dict[str, Any] = field(default_factory=dict)

    diagnostics: dict[str, Any] = field(default_factory=dict)