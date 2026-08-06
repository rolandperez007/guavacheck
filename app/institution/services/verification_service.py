from __future__ import annotations

from app.institution.services.base_service import BaseService


class VerificationService(BaseService):
    """Service for verification workflows and checks."""

    def __init__(self, db=None):
        self.db = db
        if db is not None:
            super().__init__(db)
