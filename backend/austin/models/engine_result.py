"""
Austin Engine Result
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class EngineResult:
    success: bool
    message: str

    engine: str

    confidence: float = 1.0

    metadata: dict[str, Any] = field(default_factory=dict)

    data: dict[str, Any] = field(default_factory=dict)