"""
Government Registry Stage

Future:
- Land Registry
- Surveyor General
- Governor Consent
- Deed Registry
"""

from verification_engine.orchestrator.PipelineStage import PipelineStage
from verification_engine.orchestrator.VerificationContext import VerificationContext


class RegistryStage(PipelineStage):

    async def execute(
        self,
        context: VerificationContext,
    ) -> VerificationContext:

        context.metadata["registry"] = {

            "status": "PENDING",

            "matched": False,

            "registry": None,

        }

        return context
