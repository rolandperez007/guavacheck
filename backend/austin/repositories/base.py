from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from ..models import AustinEvent


class BaseEventRepository(ABC):
    """
    Contract implemented by every Austin event repository.
    """

    @abstractmethod
    def append(self, event: AustinEvent) -> AustinEvent:
        ...

    @abstractmethod
    def list(
        self,
        *,
        window: str = "1h",
        engine: str | None = None,
        severity: str | None = None,
        category: str |None = None,
        correlation_id: str | None = None,
    ) -> list[AustinEvent]:
        ...

    @abstractmethod
    def summary(self) -> dict[str, Any]:
        ...

    @abstractmethod
    def clear(self) -> None:
        ...