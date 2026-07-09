"""
Trust Score Stage
"""

from verification_engine.orchestrator.PipelineStage import PipelineStage
from verification_engine.orchestrator.VerificationContext import VerificationContext

from verification_engine.scoring.TrustScoreEngine import TrustScoreEngine


class TrustStage(PipelineStage):

    def __init__(self):

        self.engine = TrustScoreEngine()

    async def execute(
        self,
        context: VerificationContext,
    ) -> VerificationContext:

        trust_score = self.engine.calculate(

            context.metadata

        )

        if not trust_score:

            trust_score = context.metadata.get(

                "rule_score",

                0,

            )

        context.trust_score = trust_score

        return context
