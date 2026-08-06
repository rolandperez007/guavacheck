class ForecastSimulationService:

    def predict(
        self,
        asset_id,
    ):
        return {
            "asset_id": asset_id,
            "simulation": "forecast",
        }