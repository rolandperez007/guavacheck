"""
Base Engine

Abstract base class for all guavacheck engines.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from austin.kernel import AustinKernel


class BaseEngine(ABC):
    """
    Base class for every engine.
    """

    name: str = "base"
    description: str = ""

    def __init__(self, *, kernel: AustinKernel | None = None) -> None:
        self.kernel = kernel or AustinKernel()
        self.event_publisher = self.kernel.publish_event
        self.queue = self.kernel.queue_service
        self.logger = self.kernel.logger_service
        self.incident_reporter = self.kernel.incident_reporter
        self.recommendation_engine = self.kernel.recommendation_engine

    @abstractmethod
    async def execute(self, request: dict):
        """
        Execute the engine request.
        """
        raise NotImplementedError