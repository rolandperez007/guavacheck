from __future__ import annotations

from sqlalchemy.orm import Session

from app.institution.models.institution import Institution
from app.institution.repositories.base_repository import BaseRepository


class InstitutionRepository(BaseRepository[Institution]):
    """
    Repository for institution aggregate persistence.
    """

    def __init__(self, db: Session | None = None):
        self.db = db

    def get(self, institution_id: str) -> Institution | None:
        if self.db is None:
            return None
        return self.db.query(Institution).filter(Institution.id == institution_id).first()

    def list(self) -> list[Institution]:
        if self.db is None:
            return []
        return self.db.query(Institution).all()

    def create(self, institution: Institution) -> Institution:
        if self.db is None:
            return institution
        self.db.add(institution)
        return institution

    def get_by_email(self, email: str) -> Institution | None:
        if self.db is None:
            return None
        return self.db.query(Institution).filter(Institution.email == email).first()
