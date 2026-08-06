from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class BaseWorkflowEngine(ABC):
    """
    Base interface implemented by all workflow engines.
    """

    @abstractmethod
    def execute(
        self,
        workflow,
    ):
        raise NotImplementedError

    @abstractmethod
    def pause(
        self,
        execution_id,
    ):
        raise NotImplementedError

    @abstractmethod
    def resume(
        self,
        execution_id,
    ):
        raise NotImplementedError

    @abstractmethod
    def cancel(
        self,
        execution_id,
    ):
        raise NotImplementedError