"""
Base Engine

Abstract base class for all guavacheck engines.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from backend.austin.kernel import AustinKernel


class BaseEngine(ABC):
    """
    Base class for every guavacheck engine.

    Engines share the Austin Kernel services:
    - event publishing
    - queues
    - logging
    - incidents
    - recommendations

    The AustinKernel import is deferred to avoid
    circular dependency during startup.
    """

    name: str = "base"

    description: str = ""

    def __init__(
        self,
        *,
        kernel: AustinKernel | None = None,
    ) -> None:

        if kernel is None:
            from backend.austin.kernel import AustinKernel

            kernel = AustinKernel()

        self.kernel = kernel

        self.event_publisher = self.kernel.publish_event

        self.queue = self.kernel.queue_service

        self.logger = self.kernel.logger_service

        self.incident_reporter = self.kernel.incident_reporter

        self.recommendation_engine = self.kernel.recommendation_engine

    @abstractmethod
    async def execute(
        self,
        request: dict[str, Any],
    ):
        """
        Execute the engine request.
        """

        raise NotImplementedError
