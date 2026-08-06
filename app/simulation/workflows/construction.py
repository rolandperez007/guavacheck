class ConstructionSimulationService:

    def estimate(
        self,
        project_id,
    ):
        return {
            "project_id": project_id,
            "simulation": "construction",
        }