from __future__ import annotations

from app.simulation.runtime.registry import RuntimeRegistry
from app.simulation.schemas import (
    SimulationRequest,
)


class SimulationDispatcher:
    """
    Selects the appropriate simulation
    engine for a request.
    """

    def __init__(
        self,
        registry: RuntimeRegistry,
    ) -> None:
        self.registry = registry

    def dispatch(
        self,
        request: SimulationRequest,
    ):
        engine = self.registry.resolve(
            request.engine,
        )

        return engine.simulate(
            request=request,
        )