from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class GraphHealth(BaseModel):
    """
    Overall health of a property's intelligence graph.
    """

    confidence: float = 0.0
    completeness: float = 0.0
    status: str = "UNKNOWN"

    missing_sections: list[str] = Field(default_factory=list)


class PropertyGraph(BaseModel):
    """
    Canonical Property Graph.

    This is the single object consumed by Austin,
    the Decision Engine and future Marketplace engines.
    """

    property: dict[str, Any]

    passport: dict[str, Any] | None = None

    twin: dict[str, Any] | None = None

    vision_projects: list[dict[str, Any]] = Field(default_factory=list)

    knowledge: list[dict[str, Any]] = Field(default_factory=list)

    images: list[dict[str, Any]] = Field(default_factory=list)

    engineering_snapshots: list[dict[str, Any]] = Field(default_factory=list)

    versions: list[dict[str, Any]] = Field(default_factory=list)

    mortgages: list[dict[str, Any]] = Field(default_factory=list)

    inspections: list[dict[str, Any]] = Field(default_factory=list)

    estimations: list[dict[str, Any]] = Field(default_factory=list)

    pricing_history: list[dict[str, Any]] = Field(default_factory=list)

    health: GraphHealth = Field(default_factory=GraphHealth)