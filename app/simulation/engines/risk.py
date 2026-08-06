from .base import BaseSimulationEngine


class RiskSimulationEngine(BaseSimulationEngine):
    """
    Enterprise risk simulation.

    Models operational,
    financial,
    regulatory and
    market risks.
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