"""
Verification Orchestrator

Coordinates the complete verification lifecycle
for every property submitted to guavacheck.
"""

from datetime import datetime
from verification_engine.pipeline.GovernmentStage import GovernmentStage
from verification_engine.orchestrator.VerificationContext import (
    VerificationContext,
)

from verification_engine.orchestrator.VerificationResult import (
    VerificationResult,
)

# Pipeline Stages

from verification_engine.pipeline.OCRStage import OCRStage
from verification_engine.pipeline.DocumentStage import DocumentStage
from verification_engine.pipeline.RegistryStage import RegistryStage
from verification_engine.pipeline.GeospatialStage import GeospatialStage
from verification_engine.pipeline.TimelineStage import TimelineStage
from verification_engine.pipeline.FraudStage import FraudStage
from verification_engine.pipeline.RuleStage import RuleStage
from verification_engine.pipeline.TrustStage import TrustStage
from verification_engine.pipeline.CertificateStage import CertificateStage
from verification_engine.pipeline.PersistenceStage import PersistenceStage


class VerificationOrchestrator:

    """
    Master verification workflow.

    Every verification request passes through the
    complete pipeline in a fixed order.
    """

    def __init__(self):

        self.version = "1.0"

        self.pipeline_name = "guavacheck Verification Engine"

        self.stages = [

            OCRStage(),

            GovernmentStage(),
            
            DocumentStage(),

            RegistryStage(),

            GeospatialStage(),

            TimelineStage(),

            FraudStage(),

            RuleStage(),

            TrustStage(),

            CertificateStage(),

            PersistenceStage(),

        ]

    async def verify(

        self,

        property_id: str,

        documents: list | None = None,

    ) -> VerificationResult:

        context = VerificationContext(

            property_id=property_id

        )

        context.documents = documents or []

        context.started_at = datetime.utcnow()

        context.pipeline_version = self.version

        context.pipeline_name = self.pipeline_name

        context.completed_stages = []

        for stage in self.stages:

            stage_name = stage.__class__.__name__

            context.current_stage = stage_name

            context = await stage.execute(context)

            context.completed_stages.append(stage_name)

        context.completed_at = datetime.utcnow()

        context.duration_seconds = (
            context.completed_at - context.started_at
        ).total_seconds()

        return VerificationResult(

            success=True,

            property_id=context.property_id,

            trust_score=context.trust_score,

            certificate=context.certificate,

            evidence=context.evidence,

            summary="Verification Completed Successfully",

            metadata={

                "pipeline": self.pipeline_name,

                "version": self.version,

                "completed_stages": context.completed_stages,

                "duration_seconds": context.duration_seconds,

                "verified_at": context.completed_at.isoformat(),

            },

        )
