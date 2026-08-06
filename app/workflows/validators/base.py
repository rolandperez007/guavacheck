from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class BaseWorkflowValidator(ABC):
    """
    Base validator for workflow components.
    """

    name: str = ""

    @abstractmethod
    def validate(
        self,
        workflow,
    ) -> list[str]:
        """
        Returns a list of validation errors.
        """
        raise NotImplementedError