"""
Austin Global Context

Shared context that every Austin engine receives before execution.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class GlobalContext:
    """
    Global execution context.
    """

    language: str = "en"

    locale: str = "en-US"

    country: str = "United States"

    currency: str = "USD"

    timezone: str = "UTC"

    units: str = "metric"

    measurement: str = "meters"

    region: str = "Global"

    metadata: dict = field(default_factory=dict)
