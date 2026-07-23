"""
Austin Engine Manifest

Defines the metadata every Austin engine exposes to the runtime.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class EngineManifest:
    """
    Metadata describing an Austin Engine.
    """

    # ------------------------------------------------------------------
    # Identity
    # ------------------------------------------------------------------

    name: str

    version: str

    description: str

    engine_class: str

    # ------------------------------------------------------------------
    # Runtime
    # ------------------------------------------------------------------

    priority: int = 100

    enabled: bool = True

    experimental: bool = False

    singleton: bool = True

    timeout_seconds: int = 30

    max_retries: int = 3

    # ------------------------------------------------------------------
    # Routing
    # ------------------------------------------------------------------

    intents: list[str] = field(default_factory=list)

    capabilities: list[str] = field(default_factory=list)

    keywords: list[str] = field(default_factory=list)

    supported_languages: list[str] = field(
        default_factory=lambda: ["*"]
    )

    # ------------------------------------------------------------------
    # Dependencies
    # ------------------------------------------------------------------

    requires: list[str] = field(default_factory=list)

    optional_dependencies: list[str] = field(default_factory=list)

    # ------------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------------

    owner: str = "Austin"

    tags: list[str] = field(default_factory=list)

    metadata: dict[str, Any] = field(default_factory=dict)