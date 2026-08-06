from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from app.simulation.schemas import SimulationRequest


class BaseScenario(ABC):
    """
    Base scenario definition.

    Every scenario is responsible for
    producing a SimulationRequest.
    """

    name: str = ""

    category: str = ""

    version: str = "1.0"

    @abstractmethod
    def build(self) -> SimulationRequest:
        raise NotImplementedError

    def clone(self):
        return self.__class__()

    def describe(self) -> str:
        return self.name