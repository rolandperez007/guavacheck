from __future__ import annotations

from uuid import UUID

from .coordinator import InstitutionCoordinator


class ValuationWorkflow:
    """
    Property valuation workflow.
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

        self.coordinator.vision.estimate_cost(
            property_id,
        )

        self.coordinator.austin.analyze(
            institution_id,
        )

        self.coordinator.notifications.send_email(
            institution_id,
            subject="Valuation Ready",
            body="AI valuation completed.",
        )