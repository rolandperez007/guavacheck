class MortgageSimulationService:

    def analyze(
        self,
        application_id,
    ):
        return {
            "application_id": application_id,
            "simulation": "mortgage",
        }