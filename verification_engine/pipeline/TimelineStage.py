"""
Ownership Timeline Stage
"""

from verification_engine.orchestrator.PipelineStage import PipelineStage
from verification_engine.orchestrator.VerificationContext import VerificationContext


class TimelineStage(PipelineStage):

    async def execute(
        self,
        context: VerificationContext,
    ) -> VerificationContext:

        context.metadata["timeline"] = {

            "owners": [],

            "ownership_count": 0,

            "conflicts": [],

        }

        return context
