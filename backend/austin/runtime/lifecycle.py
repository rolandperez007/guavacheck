"""
Austin Runtime Lifecycle

Tracks runtime startup and shutdown state.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(slots=True)
class RuntimeLifecycle:

    started: bool = False

    startup_time: str | None = None

    shutdown_time: str | None = None


class RuntimeLifecycleManager:

    def __init__(self):

        self._state = RuntimeLifecycle()

    def startup(self):

        self._state.started = True

        self._state.startup_time = (
            datetime.now(timezone.utc).isoformat()
        )

    def shutdown(self):

        self._state.started = False

        self._state.shutdown_time = (
            datetime.now(timezone.utc).isoformat()
        )

    @property
    def state(self):

        return self._state


runtime_lifecycle = RuntimeLifecycleManager()