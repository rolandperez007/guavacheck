"""
guavacheck Verification Service

Coordinates the complete verification workflow.
"""

from verification_engine.core.VerificationEngine import VerificationEngine
from verification_engine.document_ai.DocumentAnalyzer import DocumentAnalyzer
from verification_engine.document_ai.OCRProcessor import OCRProcessor
from verification_engine.fraud_detection.FraudDetector import FraudDetector
from verification_engine.reports.VerificationReportGenerator import (
    VerificationReportGenerator,
)
from verification_engine.scoring.TrustScoreEngine import TrustScoreEngine


class VerificationService:
    def __init__(self):

        self.engine = VerificationEngine()
        self.ocr = OCRProcessor()
        self.analyzer = DocumentAnalyzer()
        self.fraud = FraudDetector()
        self.scoring = TrustScoreEngine()
        self.reporter = VerificationReportGenerator()

    def verify_document(self, property_id: str, document_path: str):

        ocr_result = self.ocr.process_document(document_path)

        analysis = self.analyzer.analyze(
            {
                "document_type": "unknown",
                "text": ocr_result["text"],
            }
        )

        fraud = self.fraud.analyze({})

        trust = self.scoring.calculate(
            document_score=90,
            ownership_score=80,
            geospatial_score=0,
            fraud_score=fraud["fraud_score"],
        )

        verification = self.engine.verify_property(
            property_id=property_id,
            document_score=90,
            ownership_score=80,
            geospatial_score=0,
            fraud_score=fraud["fraud_score"],
        )

        report = self.reporter.generate(
            {
                "property_id": property_id,
                "final_score": verification.final_score,
                "status": verification.status,
                "warnings": verification.warnings,
            }
        )

        return {
            "verification": verification,
            "analysis": analysis,
            "trust": trust,
            "report": report,
        }
