from __future__ import annotations

from uuid import UUID


class VisionAdapter:
    """
    Adapter for the AI Vision Platform.
    """

    def create_project(
        self,
        property_id: UUID,
    ):
        raise NotImplementedError

    def render(
        self,
        project_id: UUID,
    ):
        raise NotImplementedError

    def estimate_cost(
        self,
        project_id: UUID,
    ):
        raise NotImplementedError