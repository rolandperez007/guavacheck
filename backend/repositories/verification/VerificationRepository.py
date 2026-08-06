"""
guavacheck Verification Repository

Responsible only for persistence.

The service layer decides WHAT to save.
The repository decides HOW to save it.
"""

from typing import Any

from database.connection import database


class VerificationRepository:
    def __init__(self):
        self.database = database

    def save_verification(self, verification: Any) -> dict:
        """
        Persist a verification result.

        Temporary implementation.
        Will later write to Supabase PostgreSQL.
        """

        if not self.database.connected:
            self.database.connect()

        # TODO:
        # INSERT INTO verification_records (...)

        return {
            "success": True,
            "message": "Verification saved.",
            "verification": verification,
        }

    def get_verification(self, verification_id: str) -> dict:
        """
        Retrieve a verification by ID.

        Placeholder until database integration.
        """

        if not self.database.connected:
            self.database.connect()

        return {
            "verification_id": verification_id,
            "status": "NOT_IMPLEMENTED",
        }
