"""
Austin Context Model

Shared context object passed to every Austin engine.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class AustinContext:
    session_id: str

    history: list[dict[str, Any]]

    summary: str

    world: dict[str, Any]

    metadata: dict[str, Any] = field(default_factory=dict)
