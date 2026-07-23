"""
Base Engine
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from backend.austin.models.engine_result import EngineResult


class BaseEngine(ABC):

    name: str = "base"

    @abstractmethod
    def execute(self, context) -> EngineResult:
        """
        Execute an Austin request.
        """
        raise NotImplementedError