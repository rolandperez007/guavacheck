from __future__ import annotations

from uuid import UUID

from .coordinator import InstitutionCoordinator


class InsuranceWorkflow:
    """
    Insurance underwriting workflow.
    """

    def __init__(
        self,
        coordinator: InstitutionCoordinator,
    ) -> None:
        self.coordinator = coordinator

    def execute(
        self,
        property_id: UUID,
        institution_id: UUID,
    ) -> None:

        self.coordinator.passport.get_passport(
            property_id,
        )

        self.coordinator.twin.get_twin(
            property_id,
        )

        self.coordinator.trust.risk_score(
            institution_id,
        )

        self.coordinator.decision.score(
            property_id,
        )

        self.coordinator.notifications.send_email(
            institution_id,
            subject="Insurance Assessment",
            body="Insurance workflow completed.",
        )