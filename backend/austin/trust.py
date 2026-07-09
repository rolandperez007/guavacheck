from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class CustomerTrustSnapshot:
    payment_success: float
    verification_completion: float
    search_success: float
    average_completion_time_seconds: float
    failed_customer_journeys: int
    support_ticket_trend: int

    def score(self) -> float:
        return round(
            (self.payment_success * 0.3)
            + (self.verification_completion * 0.3)
            + (self.search_success * 0.2)
            + max(0, 100 - self.average_completion_time_seconds / 10) / 100 * 0.1
            + max(0, 10 - self.failed_customer_journeys) / 10 * 0.05
            + max(0, 10 - self.support_ticket_trend) / 10 * 0.05,
            2,
        )


class TrustMonitor:
    def snapshot(self) -> dict[str, Any]:
        snapshot = CustomerTrustSnapshot(
            payment_success=97.2,
            verification_completion=94.8,
            search_success=96.1,
            average_completion_time_seconds=41.3,
            failed_customer_journeys=2,
            support_ticket_trend=4,
        )
        return {
            "score": snapshot.score(),
            "payment_success": snapshot.payment_success,
            "verification_completion": snapshot.verification_completion,
            "search_success": snapshot.search_success,
            "average_completion_time_seconds": snapshot.average_completion_time_seconds,
            "failed_customer_journeys": snapshot.failed_customer_journeys,
            "support_ticket_trend": snapshot.support_ticket_trend,
        }
