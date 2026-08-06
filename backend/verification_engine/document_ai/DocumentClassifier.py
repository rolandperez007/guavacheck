"""
guavacheck Verification Engine

Document Classification AI

Identifies property document types.
"""

from ..core.VerificationConfig import VerificationConfig


class DocumentClassifier:
    def __init__(self):

        self.supported_documents = VerificationConfig.SUPPORTED_DOCUMENTS

    def classify(self, extracted_text):
        """
        Determine the likely document category.
        """

        text = extracted_text.lower()

        if "certificate of occupancy" in text:
            return "certificate_of_occupancy"

        if "deed of assignment" in text:
            return "deed_of_assignment"

        if "survey plan" in text:
            return "survey_plan"

        if "gazette" in text:
            return "gazette"

        if "allocation letter" in text:
            return "allocation_letter"

        return "unknown"

    def confidence(self, document_type):

        if document_type == "unknown":
            return 0

        return 85
