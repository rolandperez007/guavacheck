"""
Fraud Detection Stage
"""

from verification_engine.orchestrator.PipelineStage import PipelineStage
from verification_engine.orchestrator.VerificationContext import VerificationContext

from verification_engine.fraud_detection.FraudDetector import FraudDetector
from verification_engine.fraud_detection.RiskAnalyzer import RiskAnalyzer


class FraudStage(PipelineStage):

    def __init__(self):

        self.detector = FraudDetector()
        self.risk = RiskAnalyzer()

    async def execute(
        self,
        context: VerificationContext,
    ) -> VerificationContext:

        fraud_result = self.detector.detect(context.metadata)

        risk = self.risk.analyze(context.metadata)

        context.metadata["fraud"] = fraud_result
        context.metadata["risk"] = risk

        context.evidence.append({

            "stage": "Fraud",

            "result": fraud_result,

            "risk": risk,

        })

        return context
