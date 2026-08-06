from app.simulation.engine import SimulationEngine


class SimulationCoordinator:
    """
    High-level orchestration layer for
    enterprise simulations.
    """

    def __init__(
        self,
        engine: SimulationEngine,
    ) -> None:
        self.engine = engine