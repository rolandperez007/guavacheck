from __future__ import annotations

from collections import deque
from typing import Any


class InstitutionWorker:
    """
    Executes queued institution jobs.

    Can later be connected to:

    • Redis Queue
    • Celery
    • RabbitMQ
    • Kafka
    """

    def __init__(self) -> None:
        self._queue: deque[dict[str, Any]] = deque()

    def enqueue(
        self,
        task: dict[str, Any],
    ) -> None:
        self._queue.append(task)

    def dequeue(
        self,
    ) -> dict[str, Any] | None:
        if not self._queue:
            return None

        return self._queue.popleft()

    def pending(self) -> int:
        return len(self._queue)

    def clear(self) -> None:
        self._queue.clear()

    def process(self) -> None:
        """
        Placeholder worker loop.

        Later this will dispatch tasks
        through the task registry.
        """

        while self._queue:
            task = self.dequeue()

            print(f"Executing: {task}")