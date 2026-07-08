"""
Base Engine

Abstract base class for all guavacheck engines.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class BaseEngine(ABC):
    """
    Base class for every engine.
    """

    name: str = "base"
    description: str = ""

    @abstractmethod
    async def execute(self, request: dict):
        """
        Execute the engine request.
        """
        raise NotImplementedError