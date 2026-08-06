from __future__ import annotations

from app.institution.adapters import (
    AustinAdapter,
    BillingAdapter,
    DecisionAdapter,
    NotificationAdapter,
    PassportAdapter,
    TrustAdapter,
    TwinAdapter,
    VisionAdapter,
)


class InstitutionCoordinator:
    """
    Central orchestration engine.

    Every workflow receives a coordinator
    instead of constructing adapters itself.
    """

    def __init__(self) -> None:
        self.passport = PassportAdapter()

        self.twin = TwinAdapter()

        self.vision = VisionAdapter()

        self.billing = BillingAdapter()

        self.trust = TrustAdapter()

        self.decision = DecisionAdapter()

        self.notifications = NotificationAdapter()

        self.austin = AustinAdapter()