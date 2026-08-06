class SimulationRegistry:
    """
    Registry of every simulation engine.
    """

    def __init__(self) -> None:
        self.engines = {}

    def register(
        self,
        name: str,
        engine,
    ) -> None:
        self.engines[name] = engine

    def get(
        self,
        name: str,
    ):
        return self.engines[name]