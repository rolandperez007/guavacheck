from __future__ import annotations

from app.institution.services import (
    SubscriptionService,
)


class SubscriptionTask:
    """
    Maintains institution subscriptions.
    """

    def __init__(
        self,
        service: SubscriptionService,
    ) -> None:
        self.service = service

    def run(self) -> None:
        self.service.process_expiring()

        self.service.process_renewals()

        self.service.disable_expired()