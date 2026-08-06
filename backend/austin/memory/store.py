"""
Austin Memory

Austin separates temporary conversation context from persistent
platform memory.

Context:
    Current conversation.

Memory:
    Long-term platform knowledge.

This module provides a unified interface for Austin's memory.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class MemoryRecord:
    id: str
    user_id: str
    category: str
    title: str
    value: Any
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)


class AustinMemory:
    def __init__(self):
        # Temporary in-memory implementation.
        # Future implementation will use PostgreSQL/Supabase.
        self.records: dict[str, MemoryRecord] = {}

    # --------------------------------------------------
    # CRUD
    # --------------------------------------------------

    def save(self, record: MemoryRecord | dict[str, Any]) -> MemoryRecord:
        if isinstance(record, dict):
            record = MemoryRecord(**record)

        record.updated_at = datetime.utcnow()
        self.records[record.id] = record
        return record

    def get(self, record_id: str) -> MemoryRecord | None:
        return self.records.get(record_id)

    def delete(self, record_id: str) -> None:
        self.records.pop(record_id, None)

    def exists(self, record_id: str) -> bool:
        return record_id in self.records

    # --------------------------------------------------
    # Retrieval
    # --------------------------------------------------

    def by_user(self, user_id: str) -> list[MemoryRecord]:
        return [record for record in self.records.values() if record.user_id == user_id]

    def by_category(self, category: str) -> list[MemoryRecord]:
        return [
            record for record in self.records.values() if record.category == category
        ]

    def recall(self, user_id: str) -> list[dict[str, Any]]:
        """
        Returns conversation history for a session/user.
        """

        return [
            {
                "id": record.id,
                "user_id": record.user_id,
                "category": record.category,
                "title": record.title,
                "value": record.value,
                "created_at": record.created_at.isoformat(),
                "updated_at": record.updated_at.isoformat(),
            }
            for record in sorted(
                self.by_user(user_id),
                key=lambda r: r.created_at,
            )
        ]

    def latest(
        self,
        user_id: str,
        limit: int = 20,
    ) -> list[dict[str, Any]]:
        return self.recall(user_id)[-limit:]

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

    def search(self, keyword: str) -> list[MemoryRecord]:
        keyword = keyword.lower()

        results: list[MemoryRecord] = []

        for record in self.records.values():
            if keyword in record.title.lower():
                results.append(record)
                continue

            if keyword in str(record.value).lower():
                results.append(record)

        return results

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    def count(self) -> int:
        return len(self.records)

    def categories(self) -> list[str]:
        return sorted({record.category for record in self.records.values()})

    def summary(self) -> dict[str, Any]:
        return {
            "records": self.count(),
            "categories": self.categories(),
        }


memory = AustinMemory()
