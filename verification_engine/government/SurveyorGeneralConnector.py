class SurveyorGeneralConnector:
    """
    Survey verification.

    Confirms survey plans and coordinates.
    """

    source = "Surveyor General"

    def verify(self, survey_number: str) -> dict:

        return {
            "verified": False,
            "confidence": 0.0,
            "status": "offline",
            "source": self.source,
            "survey_number": survey_number,
            "message": "Survey verification unavailable.",
        }
