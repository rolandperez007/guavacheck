class CourtJudgementConnector:
    """
    Searches court judgement databases for litigation
    affecting land ownership.
    """

    source = "Court Judgements"

    def search(self, property_id: str) -> dict:

        return {
            "source": self.source,
            "matches": [],
            "confidence": 0.0,
            "status": "offline",
            "message": "Court connector not implemented.",
            "property_id": property_id,
        }
