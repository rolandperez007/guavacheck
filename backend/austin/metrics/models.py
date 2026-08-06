"""
Austin Metrics Models

Typed models exposed to the Austin Command Center.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class QueueMetrics:
    pending: int
    processing: int
    completed: int
    failed: int


@dataclass
class EngineMetrics:
    name: str
    status: str


@dataclass
class AustinMetrics:
    platform: str
    status: str
    registered_engines: int

    queue: QueueMetrics

    engines: list[EngineMetrics] = field(default_factory=list)

    incidents: list[Any] = field(default_factory=list)

    recommendations: list[Any] = field(default_factory=list)

    events: list[Any] = field(default_factory=list)

    business: dict[str, Any] = field(default_factory=dict)
