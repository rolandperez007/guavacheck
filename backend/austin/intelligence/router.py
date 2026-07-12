"""
Austin Intelligence Router
"""

from __future__ import annotations

from .orchestrator import orchestrator


class IntelligenceRouter:

    def process(

        self,

        query: str,

    ):

        return orchestrator.execute(query)


intelligence_router = IntelligenceRouter()