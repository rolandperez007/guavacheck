from __future__ import annotations

from uuid import UUID


class DecisionAdapter:
    """
    Adapter for the Decision Engine.

    Used by banks, insurers and financial
    institutions to automate approval
    workflows.
    """

    def evaluate(
        self,
        institution_id: UUID,
        application_id: UUID,
    ):
        raise NotImplementedError

    def score(
        self,
        application_id: UUID,
    ):
        raise NotImplementedError

    def explain(
        self,
        application_id: UUID,
    ):
        raise NotImplementedError