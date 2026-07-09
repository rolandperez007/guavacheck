"""
Verification Orchestrator

This is the master workflow for the entire
guavacheck Verification Engine.
"""

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

    def __init__(self):

        self.stages = [

            OCRStage(),

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

        for stage in self.stages:

            context = await stage.execute(context)

        return VerificationResult(

            success=True,

            property_id=context.property_id,

            trust_score=context.trust_score,

            certificate=context.certificate,

            evidence=context.evidence,

            summary="Verification Completed Successfully",

        )
