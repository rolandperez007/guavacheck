from __future__ import annotations

from app.simulation.runtime.dispatcher import (
    SimulationDispatcher,
)
from app.simulation.schemas import (
    SimulationRequest,
)


class SimulationPipeline:
    """
    End-to-end execution pipeline.
    """

    def __init__(
        self,
        dispatcher: SimulationDispatcher,
    ) -> None:
        self.dispatcher = dispatcher

    def execute(
        self,
        request: SimulationRequest,
    ):
        return self.dispatcher.dispatch(
            request,
        )