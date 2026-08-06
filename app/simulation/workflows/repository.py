from __future__ import annotations

from uuid import UUID


class SimulationWorkflowRepository:
    """
    Repository for simulation workflow requests.
    """

    def list_by_reference(
        self,
        reference_id: UUID,
    ):
        raise NotImplementedError

    def save(
        self,
        simulation,
    ):
        raise NotImplementedError