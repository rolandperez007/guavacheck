class RiskSimulationService:

    def score(
        self,
        reference_id,
    ):
        return {
            "reference_id": reference_id,
            "simulation": "risk",
        }