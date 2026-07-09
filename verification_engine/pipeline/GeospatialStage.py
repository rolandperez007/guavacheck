"""
GIS Validation Stage
"""

from verification_engine.orchestrator.PipelineStage import PipelineStage
from verification_engine.orchestrator.VerificationContext import VerificationContext


class GeospatialStage(PipelineStage):

    async def execute(
        self,
        context: VerificationContext,
    ) -> VerificationContext:

        context.metadata["geospatial"] = {

            "coordinates_valid": False,

            "parcel_match": False,

            "overlap_detected": False,

        }

        return context
