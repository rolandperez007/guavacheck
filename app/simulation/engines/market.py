from .base import BaseSimulationEngine


class MarketSimulationEngine(BaseSimulationEngine):
    """
    Property market simulation.

    Models demand, supply,
    pricing, absorption,
    appreciation and cycles.
    """

    def simulate(self, **kwargs):
        raise NotImplementedError

    def forecast(self, **kwargs):
        raise NotImplementedError

    def compare(self, **kwargs):
        raise NotImplementedError

    def optimize(self, **kwargs):
        raise NotImplementedError

    def report(self, **kwargs):
        raise NotImplementedError