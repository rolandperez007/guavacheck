"""
Ownership History Engine

Builds historical ownership records
for a property.
"""

from __future__ import annotations

from datetime import datetime


class OwnershipHistory:
    def __init__(self):

        self.history = []

    def add_record(
        self,
        owner: str,
        title_number: str,
        acquired_date: datetime,
    ):

        self.history.append(
            {
                "owner": owner,
                "title_number": title_number,
                "acquired_date": acquired_date,
            }
        )

    def get_history(self):

        return self.history

    def latest_owner(self):

        if not self.history:
            return None

        return self.history[-1]
