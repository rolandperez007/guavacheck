"""
Austin Context Manager

Tracks temporary conversation context for Austin sessions.
"""

from __future__ import annotations

from typing import Any


class AustinContextManager:
    def __init__(self) -> None:
        self._contexts: dict[str, dict[str, Any]] = {}

    def get(self, session_id: str) -> dict[str, Any]:
        return self._contexts.setdefault(session_id, {})

    def set(self, session_id: str, key: str, value: Any) -> None:
        self.get(session_id)[key] = value

    def clear(self, session_id: str) -> None:
        self._contexts.pop(session_id, None)

    def snapshot(self) -> dict[str, dict[str, Any]]:
        return dict(self._contexts)


context_manager = AustinContextManager()
