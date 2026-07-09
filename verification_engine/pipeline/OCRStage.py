"""
OCR Pipeline Stage

Extracts text from uploaded documents.
"""

from verification_engine.orchestrator.PipelineStage import PipelineStage
from verification_engine.orchestrator.VerificationContext import VerificationContext

from verification_engine.document_ai.OCRProcessor import OCRProcessor


class OCRStage(PipelineStage):

    def __init__(self):

        self.ocr = OCRProcessor()

    async def execute(
        self,
        context: VerificationContext,
    ) -> VerificationContext:

        extracted_documents = []

        for document in context.documents:

            result = self.ocr.process(document)

            extracted_documents.append(result)

        context.metadata["ocr"] = extracted_documents

        return context
