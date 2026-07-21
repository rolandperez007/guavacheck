"""
Austin Metrics Service

Collects operational metrics for the Austin Command Center.
"""

from __future__ import annotations

from .models import AustinMetrics
from .models import QueueMetrics
from .models import EngineMetrics
from ..status import status
from ..queue import queue
from ..registry import registry
from ..event_store import store
from ..incident_manager import manager
from ..business_monitor import monitor
from ..recommendations import AustinRecommendations


class AustinMetricsService:

    def collect(self) -> AustinMetrics:

        recommendation_engine = AustinRecommendations()

        return AustinMetrics(

            platform="guavacheck",

            status="healthy" if status.healthy else "degraded",

            registered_engines=status.registered_engines,

            queue=QueueMetrics(

                pending=queue.pending,

                processing=queue.processing,

                completed=queue.completed,

                failed=queue.failed,

            ),

            engines=[

                EngineMetrics(

                    name=e.name,

                    status="active",

                )

                for e in registry.engines.values()

            ],

            incidents=manager.active_incidents(),

            recommendations=recommendation_engine.generate(),

            events=store.latest(20),

            business=monitor.snapshot(),

        )


metrics = AustinMetricsService()