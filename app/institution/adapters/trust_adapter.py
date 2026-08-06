from __future__ import annotations

from uuid import UUID


class TrustAdapter:
    """
    Adapter for Trust &
    Verification services.
    """

    def verify_identity(
        self,
        institution_id: UUID,
    ):
        raise NotImplementedError

    def verify_license(
        self,
        institution_id: UUID,
    ):
        raise NotImplementedError

    def verify_documents(
        self,
        institution_id: UUID,
    ):
        raise NotImplementedError

    def risk_score(
        self,
        institution_id: UUID,
    ):
        raise NotImplementedError