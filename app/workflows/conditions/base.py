from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class BaseCondition(ABC):
    """
    Base workflow condition.
    """

    name: str = ""

    @abstractmethod
    def evaluate(
        self,
        context,
    ) -> bool:
        raise NotImplementedError