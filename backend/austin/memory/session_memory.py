"""
Austin Session Memory
"""

from __future__ import annotations

from collections import defaultdict


class SessionMemory:
    def __init__(self):

        self._memory = defaultdict(list)

    def add(
        self,
        session_id: str,
        role: str,
        message: str,
    ):

        self._memory[session_id].append(
            {
                "role": role,
                "message": message,
            }
        )

    def history(
        self,
        session_id: str,
    ):

        return self._memory.get(
            session_id,
            [],
        )

    def clear(
        self,
        session_id: str,
    ):

        self._memory.pop(
            session_id,
            None,
        )


session_memory = SessionMemory()
