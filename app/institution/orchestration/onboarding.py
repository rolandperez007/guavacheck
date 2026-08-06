from __future__ import annotations

from uuid import UUID

from .coordinator import InstitutionCoordinator


class InstitutionOnboardingWorkflow:
    """
    Institution onboarding workflow.

    Flow

    Registration
        ↓
    Verification
        ↓
    Compliance
        ↓
    Subscription
        ↓
    Welcome
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

        self.coordinator.trust.verify_documents(
            institution_id,
        )

        self.coordinator.billing.subscription(
            institution_id,
        )

        self.coordinator.notifications.send_email(
            institution_id,
            subject="Welcome to Guava",
            body="Institution onboarding completed.",
        )