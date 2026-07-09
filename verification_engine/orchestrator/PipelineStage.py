"""
Pipeline Stage

Every pipeline module derives from this class.
"""

from abc import ABC
from abc import abstractmethod

from verification_engine.orchestrator.VerificationContext import (
    VerificationContext,
)


class PipelineStage(ABC):

    @abstractmethod
    async def execute(

        self,

        context: VerificationContext,

    ) -> VerificationContext:

        pass
