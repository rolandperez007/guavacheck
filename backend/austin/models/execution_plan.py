"""
Austin Execution Plan
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ExecutionPlan:
    intent: str
    engine: str
    priority: str = "normal"
    background: bool = True
    confidence: float = 1.0
