from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class RoutingDecision:
    """
    Output returned by GatewayIntelligence.
    """

    route: str
    execution_mode: str
    confidence: float
    reason: str


class GatewayIntelligence:
    """
    Central routing brain for Austin.

    Responsibilities:
    - Understand user intent
    - Determine execution path
    - Decide sync vs async
    - Select appropriate subsystem

    Does NOT:
    - Execute jobs
    - Call agents directly
    - Access databases
    - Generate reports
    """

    def classify(
        self, query: str, context: dict[str, Any] | None = None
    ) -> RoutingDecision:
        query_lower = query.lower()

        # ------------------------------------
        # PDF / Export Requests
        # ------------------------------------
        if any(
            keyword in query_lower
            for keyword in [
                "export report",
                "download pdf",
                "generate pdf",
                "create report",
            ]
        ):
            return RoutingDecision(
                route="pdf_export",
                execution_mode="async",
                confidence=0.98,
                reason="Heavy report generation detected.",
            )

        # ------------------------------------
        # BOQ / Construction
        # ------------------------------------
        if any(
            keyword in query_lower
            for keyword in [
                "boq",
                "bill of quantities",
                "construction cost",
                "building estimate",
            ]
        ):
            return RoutingDecision(
                route="construction",
                execution_mode="async",
                confidence=0.95,
                reason="Construction estimation workflow.",
            )

        # ------------------------------------
        # Escrow
        # ------------------------------------
        if any(
            keyword in query_lower
            for keyword in [
                "escrow",
                "release funds",
                "milestone payment",
                "contract payment",
            ]
        ):
            return RoutingDecision(
                route="escrow",
                execution_mode="async",
                confidence=0.95,
                reason="Escrow workflow detected.",
            )

        # ------------------------------------
        # Mortgage
        # ------------------------------------
        if any(
            keyword in query_lower
            for keyword in [
                "mortgage",
                "monthly payment",
                "loan repayment",
                "interest rate",
            ]
        ):
            return RoutingDecision(
                route="mortgage",
                execution_mode="sync",
                confidence=0.92,
                reason="Mortgage calculation request.",
            )

        # ------------------------------------
        # Property Search
        # ------------------------------------
        if any(
            keyword in query_lower
            for keyword in [
                "find property",
                "search property",
                "buy house",
                "rent apartment",
                "property listing",
            ]
        ):
            return RoutingDecision(
                route="listing",
                execution_mode="sync",
                confidence=0.90,
                reason="Property discovery request.",
            )

        # ------------------------------------
        # Design / Architecture
        # ------------------------------------
        if any(
            keyword in query_lower
            for keyword in [
                "house design",
                "floor plan",
                "architectural drawing",
                "3d design",
            ]
        ):
            return RoutingDecision(
                route="design",
                execution_mode="async",
                confidence=0.94,
                reason="Design generation workflow.",
            )

        # ------------------------------------
        # Investment Analysis
        # ------------------------------------
        if any(
            keyword in query_lower
            for keyword in [
                "roi",
                "investment",
                "cash flow",
                "rental yield",
            ]
        ):
            return RoutingDecision(
                route="investment",
                execution_mode="sync",
                confidence=0.91,
                reason="Investment analysis request.",
            )

        # ------------------------------------
        # Default Austin Conversation
        # ------------------------------------
        return RoutingDecision(
            route="austin_chat",
            execution_mode="sync",
            confidence=0.70,
            reason="General Austin conversation.",
        )

    def should_queue(self, decision: RoutingDecision) -> bool:
        """
        Determines if request should become a background job.
        """

        return decision.execution_mode == "async"

    def get_route(self, query: str) -> str:
        """
        Convenience helper.
        """

        decision = self.classify(query)
        return decision.route
