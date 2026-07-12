"""
Austin Conversation Repository

Provides persistence for Austin conversations.

For now this is an in-memory implementation.

Later this class can be swapped for:
    • PostgreSQL
    • Supabase
    • Redis
    • MongoDB
without changing the Austin Engine.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Any


class ConversationRepository:

    def __init__(self):

        self._sessions = defaultdict(list)

    def append(
        self,
        session_id: str,
        role: str,
        message: str,
    ) -> None:

        self._sessions[session_id].append(
            {
                "role": role,
                "message": message,
            }
        )

    def history(
        self,
        session_id: str,
    ) -> list[dict[str, Any]]:

        return list(
            self._sessions.get(
                session_id,
                [],
            )
        )

    def clear(
        self,
        session_id: str,
    ) -> None:

        self._sessions.pop(
            session_id,
            None,
        )

    def sessions(self) -> list[str]:

        return sorted(
            self._sessions.keys()
        )


conversation_repository = ConversationRepository()