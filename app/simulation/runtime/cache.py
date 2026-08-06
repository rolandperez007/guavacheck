from __future__ import annotations

from typing import Any


class SimulationCache:
    """
    Runtime cache abstraction.

    Can later use:

    • Redis

    • Memcached

    • Local Memory

    • Disk

    without changing engines.
    """

    def __init__(self) -> None:
        self._cache: dict[str, Any] = {}

    def get(
        self,
        key: str,
    ) -> Any:
        return self._cache.get(key)

    def put(
        self,
        key: str,
        value: Any,
    ) -> None:
        self._cache[key] = value

    def clear(self) -> None:
        self._cache.clear()