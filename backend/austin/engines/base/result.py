"""
Austin Engine Result
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class EngineResult:
    success: bool

    engine: str

    response: str

    confidence: float = 1.0

    diagnostics: dict[str, Any] = field(default_factory=dict)

    metadata: dict[str, Any] = field(default_factory=dict)
