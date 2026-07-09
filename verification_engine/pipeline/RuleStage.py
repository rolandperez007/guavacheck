"""
Business Rule Engine Stage
"""

from verification_engine.orchestrator.PipelineStage import PipelineStage
from verification_engine.orchestrator.VerificationContext import VerificationContext


class RuleStage(PipelineStage):

    async def execute(
        self,
        context: VerificationContext,
    ) -> VerificationContext:

        score = 100

        fraud = context.metadata.get("fraud", {})

        if fraud.get("fraud_detected"):

            score -= 50

        registry = context.metadata.get("registry", {})

        if not registry.get("matched"):

            score -= 20

        geo = context.metadata.get("geospatial", {})

        if geo.get("overlap_detected"):

            score -= 15

        if not geo.get("coordinates_valid"):

            score -= 15

        context.metadata["rule_score"] = max(score, 0)

        return context
