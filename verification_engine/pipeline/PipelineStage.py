"""
Pipeline Stage Base Class

Defines the contract for all verification
engine pipeline stages.

Every stage receives a VerificationContext
and returns the updated context.
"""


from abc import ABC, abstractmethod


class PipelineStage(ABC):


    @abstractmethod
    async def execute(
        self,
        context,
    ):

        """
        Execute pipeline stage.

        Args:
            context:
                VerificationContext instance

        Returns:
            Updated VerificationContext
        """

        raise NotImplementedError