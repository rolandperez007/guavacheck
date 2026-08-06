"""
Austin Runtime Router
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class AustinRouteResult:
    engine: str
    confidence: float = 1.0


class AustinRouter:
    def route(self, context):
        """
        Placeholder routing.

        Eventually this will use
        planner +
        dispatcher +
        engine registry.
        """

        return AustinRouteResult(engine="conversation")


router = AustinRouter()
