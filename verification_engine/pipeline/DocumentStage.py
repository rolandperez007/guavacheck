"""
Document Analysis Stage
"""

from verification_engine.orchestrator.PipelineStage import PipelineStage
from verification_engine.orchestrator.VerificationContext import VerificationContext

from verification_engine.document_ai.DocumentAnalyzer import DocumentAnalyzer
from verification_engine.document_ai.DocumentClassifier import DocumentClassifier


class DocumentStage(PipelineStage):

    def __init__(self):

        self.analyzer = DocumentAnalyzer()
        self.classifier = DocumentClassifier()

    async def execute(
        self,
        context: VerificationContext,
    ) -> VerificationContext:

        analysis = []

        ocr_results = context.metadata.get("ocr", [])

        for item in ocr_results:

            report = self.analyzer.analyze(item)

            category = self.classifier.classify(item)

            analysis.append({

                "analysis": report,

                "classification": category,

            })

        context.metadata["documents"] = analysis

        return context
