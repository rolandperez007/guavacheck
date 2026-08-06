from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class BaseWorkflowTemplate(ABC):
    """
    Base class for reusable workflow templates.
    """

    name: str = ""

    category: str = ""

    description: str = ""

    @abstractmethod
    def build(self):
        """
        Returns a WorkflowSchema.
        """
        raise NotImplementedError