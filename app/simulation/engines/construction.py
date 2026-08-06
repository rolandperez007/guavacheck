from .base import BaseSimulationEngine


class ConstructionSimulationEngine(BaseSimulationEngine):
    """
    Construction cost, schedule,
    inflation and BOQ simulation.
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