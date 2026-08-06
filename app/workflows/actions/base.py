from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class BaseWorkflowAction(ABC):
    """
    Base class for all workflow actions.
    """

    name: str = ""

    @abstractmethod
    def execute(
        self,
        context,
    ):
        raise NotImplementedError