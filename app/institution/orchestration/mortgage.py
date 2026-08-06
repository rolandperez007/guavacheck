from __future__ import annotations

from uuid import UUID

from .coordinator import InstitutionCoordinator


class MortgageWorkflow:
    """
    Mortgage approval pipeline.

    Passport

        ↓

    Digital Twin

        ↓

    Decision Engine

        ↓

    Billing

        ↓

    Notification
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

        self.coordinator.passport.create_passport(
            property_id,
        )

        self.coordinator.twin.create_twin(
            property_id,
        )

        self.coordinator.decision.evaluate(
            institution_id,
            property_id,
        )

        self.coordinator.notifications.send_email(
            institution_id,
            subject="Mortgage Evaluation",
            body="Mortgage workflow completed.",
        )