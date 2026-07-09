"""
Certificate Generation Stage
"""

import uuid

from verification_engine.orchestrator.PipelineStage import PipelineStage
from verification_engine.orchestrator.VerificationContext import VerificationContext


class CertificateStage(PipelineStage):

    async def execute(
        self,
        context: VerificationContext,
    ) -> VerificationContext:

        context.certificate = {

            "certificate_id": str(uuid.uuid4()),

            "trust_score": context.trust_score,

            "status": (

                "VERIFIED"

                if context.trust_score >= 80

                else "REVIEW_REQUIRED"

            ),

        }

        return context
