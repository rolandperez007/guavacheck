from .base import BaseSimulationEngine


class ValuationSimulationEngine(BaseSimulationEngine):
    """
    Property valuation scenarios.
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