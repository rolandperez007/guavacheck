from .base import BaseSimulationEngine


class MonteCarloSimulationEngine(BaseSimulationEngine):
    """
    Monte Carlo engine.

    Performs probabilistic
    simulations across thousands
    of randomized scenarios.
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