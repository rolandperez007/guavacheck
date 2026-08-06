from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class InstitutionMetrics:
    """
    Institution analytics snapshot.
    """

    institutions: int = 0

    active_institutions: int = 0

    verified_institutions: int = 0

    branches: int = 0

    members: int = 0

    products: int = 0

    subscriptions: int = 0

    monthly_revenue: float = 0.0

    api_requests: int = 0

    verification_requests: int = 0

    successful_verifications: int = 0

    failed_verifications: int = 0

    active_integrations: int = 0

    webhooks_sent: int = 0

    invitations_sent: int = 0

    invitations_accepted: int = 0

    audits_generated: int = 0