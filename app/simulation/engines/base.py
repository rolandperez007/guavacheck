from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class BaseSimulationEngine(ABC):
    """
    Base class for every simulation engine.

    Every engine follows exactly the same API.
    """

    @abstractmethod
    def simulate(
        self,
        **kwargs,
    ):
        raise NotImplementedError

    @abstractmethod
    def forecast(
        self,
        **kwargs,
    ):
        raise NotImplementedError

    @abstractmethod
    def compare(
        self,
        **kwargs,
    ):
        raise NotImplementedError

    @abstractmethod
    def optimize(
        self,
        **kwargs,
    ):
        raise NotImplementedError

    @abstractmethod
    def report(
        self,
        **kwargs,
    ):
        raise NotImplementedError