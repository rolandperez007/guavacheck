"""
Austin Engine Definition

Every engine registers itself using this model.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class Engine:
    name: str

    version: str

    description: str

    category: str

    entrypoint: object

    capabilities: list[str] = field(default_factory=list)

    supported_languages: list[str] = field(default_factory=lambda: ["en"])

    supported_countries: list[str] = field(default_factory=lambda: ["*"])

    priority: int = 100

    enabled: bool = True

    healthy: bool = True
