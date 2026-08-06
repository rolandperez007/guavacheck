class ValuationSimulationService:

    def evaluate(
        self,
        passport_id,
    ):
        return {
            "passport_id": passport_id,
            "simulation": "valuation",
        }