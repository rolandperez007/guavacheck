from __future__ import annotations

from app.simulation.engines.base import BaseSimulationEngine


class RuntimeRegistry:
    """
    Runtime engine registry.
    """

    def __init__(self) -> None:
        self._engines: dict[
            str,
            BaseSimulationEngine,
        ] = {}

    def register(
        self,
        name: str,
        engine: BaseSimulationEngine,
    ) -> None:
        self._engines[name] = engine

    def resolve(
        self,
        name: str,
    ) -> BaseSimulationEngine:
        return self._engines[name]