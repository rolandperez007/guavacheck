from __future__ import annotations

from uuid import UUID

from .coordinator import InstitutionCoordinator


class ComplianceWorkflow:
    """
    Regulatory compliance workflow.
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

        self.coordinator.trust.verify_documents(
            institution_id,
        )

        self.coordinator.trust.verify_license(
            institution_id,
        )

        self.coordinator.austin.summarize(
            institution_id,
        )

        self.coordinator.notifications.send_email(
            institution_id,
            subject="Compliance Review",
            body="Compliance review completed.",
        )