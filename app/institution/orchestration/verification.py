from __future__ import annotations

from uuid import UUID

from .coordinator import InstitutionCoordinator


class VerificationWorkflow:
    """
    Institution verification workflow.

    Identity
        ↓
    Licenses
        ↓
    Documents
        ↓
    Risk Assessment
        ↓
    Decision
    """

    def __init__(
        self,
        coordinator: InstitutionCoordinator,
    ) -> None:
        self.coordinator = coordinator

    def execute(
        self,
        institution_id: UUID,
    ) -> None:

        self.coordinator.trust.verify_identity(
            institution_id,
        )

        self.coordinator.trust.verify_license(
            institution_id,
        )

        self.coordinator.trust.verify_documents(
            institution_id,
        )

        self.coordinator.trust.risk_score(
            institution_id,
        )

        self.coordinator.notifications.send_email(
            institution_id,
            subject="Verification Complete",
            body="Institution verification has completed.",
        )