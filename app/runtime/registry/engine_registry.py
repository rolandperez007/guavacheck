"""
Enterprise Engine Registry

Provides a single location where
every platform engine is instantiated.
"""

from app.property.engines.graph_engine import (
    PropertyGraphEngine,
)


class EngineRegistry:

    def __init__(self):

        self.graph = PropertyGraphEngine()

        #
        # Future
        #

        # self.decision = DecisionEngine()

        # self.simulation = SimulationEngine()

        # self.marketplace = MarketplaceEngine()