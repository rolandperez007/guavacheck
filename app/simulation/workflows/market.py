class MarketSimulationService:

    def evaluate(
        self,
        location_id,
    ):
        return {
            "location_id": location_id,
            "simulation": "market",
        }