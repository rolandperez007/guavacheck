from __future__ import annotations

from app.institution.analytics import (
    InstitutionMetrics,
)


class AnalyticsTask:
    """
    Rebuild institution analytics.
    """

    def __init__(
        self,
        metrics: InstitutionMetrics,
    ) -> None:
        self.metrics = metrics

    def run(self) -> None:
        self.metrics.refresh()