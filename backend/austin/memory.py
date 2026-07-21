"""
Austin Memory

Unified memory layer for Austin.

Supports both:
- Persistent record storage
- Conversation history compatibility
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

        self.records: dict[str, MemoryRecord] = {}

    # --------------------------------------------------
    # CRUD
    # --------------------------------------------------

    def save(self, record: MemoryRecord | dict[str, Any]):

        if isinstance(record, dict):
            record = MemoryRecord(**record)

        record.updated_at = datetime.utcnow()

        self.records[record.id] = record

        return record

    def get(self, record_id: str):

        return self.records.get(record_id)

    def delete(self, record_id: str):

        self.records.pop(record_id, None)

    def exists(self, record_id: str):

        return record_id in self.records

    # --------------------------------------------------
    # Conversation Compatibility
    # --------------------------------------------------

    def remember(
        self,
        session_id: str,
        role: str,
        message: str,
    ):

        self.save(
            {
                "id": f"{session_id}:{self.count()}",
                "user_id": session_id,
                "category": "conversation",
                "title": role,
                "value": message,
            }
        )

    def recall(
        self,
        session_id: str,
    ):

        history = []

        for record in self.by_user(session_id):

            if record.category == "conversation":

                history.append(
                    {
                        "role": record.title,
                        "message": record.value,
                    }
                )

        return history

    def forget(
        self,
        session_id: str,
    ):

        for key in list(self.records.keys()):

            if self.records[key].user_id == session_id:

                del self.records[key]

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

    def by_user(self, user_id: str):

        return [
            record
            for record in self.records.values()
            if record.user_id == user_id
        ]

    def by_category(self, category: str):

        return [
            record
            for record in self.records.values()
            if record.category == category
        ]

    def search(self, keyword: str):

        keyword = keyword.lower()

        results = []

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

    def count(self):

        return len(self.records)

    def categories(self):

        return sorted(
            {
                record.category
                for record in self.records.values()
            }
        )

    def summary(self):

        return {
            "records": self.count(),
            "categories": self.categories(),
        }


memory = AustinMemory()