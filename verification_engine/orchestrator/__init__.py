"""
Verification Orchestrator Package
"""

"""
Pipeline Stage

Base class for every verification stage.
"""

from abc import ABC, abstractmethod


class PipelineStage(ABC):
    @abstractmethod
    async def execute(
        self,
        context: dict,
    ) -> dict:
        """
        Execute a verification stage.
        """
        raise NotImplementedError
