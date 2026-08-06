"""
Austin Memory Manager

Central interface used by Austin to access
conversation history.
"""

from __future__ import annotations

from .session_memory import session_memory


class MemoryManager:
    def remember(
        self,
        session_id: str,
        role: str,
        message: str,
    ):

        session_memory.add(
            session_id,
            role,
            message,
        )

    def recall(
        self,
        session_id: str,
    ):

        return session_memory.history(
            session_id,
        )

    def forget(
        self,
        session_id: str,
    ):

        session_memory.clear(
            session_id,
        )


memory = MemoryManager()
