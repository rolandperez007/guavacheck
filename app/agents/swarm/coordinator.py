from app.agents.swarm.pricing_agent import PricingAgent
from app.agents.swarm.insight_agent import InsightAgent
from app.agents.swarm.ranking_agent import RankingAgent


class SwarmCoordinator:

    def __init__(self):

        self.pricing = PricingAgent()
        self.insight = InsightAgent()
        self.ranking = RankingAgent()

    def enrich_property(self, property_data):

        property_data["pricing"] = self.pricing.analyze(property_data)

        property_data["insight"] = self.insight.analyze(property_data)

        property_data["score"] = self.ranking.score(property_data)

        return property_data