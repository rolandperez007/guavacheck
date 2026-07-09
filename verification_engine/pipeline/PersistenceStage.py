"""
Persistence Stage

Stores verification results.
"""

from verification_engine.orchestrator.PipelineStage import PipelineStage
from verification_engine.orchestrator.VerificationContext import VerificationContext

from repositories.verification.VerificationRepository import (
    VerificationRepository,
)


class PersistenceStage(PipelineStage):

    def __init__(self):

        self.repository = VerificationRepository()

    async def execute(
        self,
        context: VerificationContext,
    ) -> VerificationContext:

        self.repository.save(

            property_id=context.property_id,

            trust_score=context.trust_score,

            certificate=context.certificate,

            evidence=context.evidence,

        )

        return context
