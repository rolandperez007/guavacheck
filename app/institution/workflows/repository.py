from __future__ import annotations

from uuid import UUID


class InstitutionWorkflowRepository:
    """
    Repository responsible for institution workflow persistence.
    """

    def workflows(
        self,
        institution_id: UUID,
    ):
        raise NotImplementedError

    def save(
        self,
        workflow,
    ):
        raise NotImplementedError

    def delete(
        self,
        workflow_id: UUID,
    ):
        raise NotImplementedError