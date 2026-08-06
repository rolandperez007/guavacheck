from __future__ import annotations

from sqlalchemy.orm import Session

from app.institution.repositories.institution_repository import InstitutionRepository
from app.institution.services.base_service import BaseService


class InstitutionService(BaseService):
    """
    Service layer for institution lifecycle and domain operations.
    """

    def __init__(self, repository: InstitutionRepository, db: Session | None = None):
        self.repository = repository
        self.db = repository.db if repository.db is not None else db
        if self.db is not None:
            super().__init__(self.db)

    def list(self):
        return self.repository.list()

    def get(self, institution_id: str):
        return self.repository.get(institution_id)

    def create(self, institution):
        return self.repository.create(institution)

    def get_by_email(self, email: str):
        return self.repository.get_by_email(email)
