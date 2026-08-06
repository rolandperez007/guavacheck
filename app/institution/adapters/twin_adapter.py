from __future__ import annotations

from uuid import UUID


class TwinAdapter:
    """
    Adapter for the Digital Twin engine.
    """

    def create_twin(
        self,
        property_id: UUID,
    ):
        raise NotImplementedError

    def synchronize(
        self,
        twin_id: UUID,
    ):
        raise NotImplementedError

    def get_twin(
        self,
        twin_id: UUID,
    ):
        raise NotImplementedError