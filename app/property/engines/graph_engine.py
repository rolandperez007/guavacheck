from __future__ import annotations

from app.property.repositories.graph_repository import (
    PropertyGraphRepository,
)
from app.property.schemas.graph import PropertyGraph


class PropertyGraphEngine:
    """
    Enterprise Property Graph Engine.

    Every AI capability should consume
    a PropertyGraph rather than querying
    repositories individually.
    """

    def __init__(self):

        self.repository = PropertyGraphRepository()

    def build(self, property_id: str) -> PropertyGraph:

        graph = self.repository.load(property_id)

        self._calculate_completeness(graph)

        self._calculate_confidence(graph)

        return graph

    def _calculate_completeness(
        self,
        graph: PropertyGraph,
    ) -> None:

        sections = [
            graph.passport,
            graph.twin,
            graph.vision_projects,
            graph.images,
            graph.engineering_snapshots,
            graph.knowledge,
            graph.pricing_history,
        ]

        total = len(sections)

        complete = sum(1 for section in sections if section)

        graph.health.completeness = (complete / total) * 100

    def _calculate_confidence(
        self,
        graph: PropertyGraph,
    ) -> None:

        confidence = 100.0

        missing = []

        if not graph.passport:
            confidence -= 15

            missing.append("passport")

        if not graph.twin:
            confidence -= 15

            missing.append("twin")

        if not graph.images:
            confidence -= 10

            missing.append("images")

        if not graph.vision_projects:
            confidence -= 10

            missing.append("vision")

        if not graph.engineering_snapshots:
            confidence -= 15

            missing.append("engineering")

        if not graph.pricing_history:
            confidence -= 5

            missing.append("pricing")

        if not graph.knowledge:
            confidence -= 10

            missing.append("knowledge")

        graph.health.confidence = max(
            confidence,
            0,
        )

        graph.health.missing_sections = missing

        if confidence >= 90:
            graph.health.status = "EXCELLENT"

        elif confidence >= 75:
            graph.health.status = "GOOD"

        elif confidence >= 50:
            graph.health.status = "FAIR"

        else:
            graph.health.status = "POOR"
