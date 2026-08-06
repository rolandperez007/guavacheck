from app.simulation.registry import SimulationRegistry


class SimulationEngine:
    """
    Root simulation engine.

    Coordinates every simulation module.
    """

    def __init__(self) -> None:
        self.registry = SimulationRegistry()