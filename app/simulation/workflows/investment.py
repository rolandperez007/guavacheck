class InvestmentSimulationService:

    def project(
        self,
        investment_id,
    ):
        return {
            "investment_id": investment_id,
            "simulation": "investment",
        }