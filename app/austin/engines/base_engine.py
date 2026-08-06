"""
Austin Base Engine

Defines the common interface
implemented by every Austin engine.
"""

from abc import ABC
from abc import abstractmethod


class BaseEngine(ABC):

    @property
    @abstractmethod
    def name(self):
        """Unique engine name."""
        pass

    @abstractmethod
    def execute(
        self,
        request,
    ):
        """
        Execute a request.

        Returns a dictionary.
        """
        pass

    def health(self):
        return {
            "engine": self.name,
            "status": "online",
        }