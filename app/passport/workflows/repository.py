from __future__ import annotations

from uuid import UUID


class PassportWorkflowRepository:
    """
    Persistence layer for passport workflows.
    """

    def list_for_passport(
        self,
        passport_id: UUID,
    ):
        raise NotImplementedError

    def save(
        self,
        workflow,
    ):
        raise NotImplementedError