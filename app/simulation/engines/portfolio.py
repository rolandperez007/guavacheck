from .base import BaseSimulationEngine


class PortfolioSimulationEngine(BaseSimulationEngine):
    """
    Portfolio optimization engine.

    Evaluates institutional
    property portfolios and
    investment allocations.
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