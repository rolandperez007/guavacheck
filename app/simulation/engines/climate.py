from .base import BaseSimulationEngine


class ClimateSimulationEngine(BaseSimulationEngine):
    """
    Climate impact simulator.

    Models flooding,
    erosion,
    heat,
    rainfall,
    sea level
    and environmental exposure.
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