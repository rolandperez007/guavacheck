from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class BaseWorkflowTrigger(ABC):
    """
    Base class for all workflow triggers.
    """

    name: str = ""

    @abstractmethod
    def should_fire(
        self,
        event,
    ) -> bool:
        raise NotImplementedError

    @abstractmethod
    def fire(
        self,
        context,
    ):
        raise NotImplementedError