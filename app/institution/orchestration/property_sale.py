from __future__ import annotations

from uuid import UUID

from .coordinator import InstitutionCoordinator


class PropertySaleWorkflow:
    """
    Property sale workflow.

    Passport
        ↓
    Twin
        ↓
    Vision
        ↓
    Decision
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

        self.coordinator.vision.create_project(
            property_id,
        )

        self.coordinator.decision.evaluate(
            institution_id,
            property_id,
        )

        self.coordinator.billing.create_invoice(
            institution_id,
        )

        self.coordinator.notifications.send_email(
            institution_id,
            subject="Property Sale Complete",
            body="Property workflow completed.",
        )