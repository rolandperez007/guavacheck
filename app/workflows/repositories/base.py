from __future__ import annotations

from sqlalchemy.orm import Session


class BaseRepository:
    """
    Base repository for workflow persistence.

    All workflow repositories inherit from this class.
    """

    model = None

    def __init__(
        self,
        session: Session,
    ) -> None:
        self.session = session

    def add(
        self,
        entity,
    ):
        self.session.add(entity)
        return entity

    def get(
        self,
        entity_id,
    ):
        return self.session.get(
            self.model,
            entity_id,
        )

    def list(self):
        return (
            self.session.query(self.model)
            .all()
        )

    def delete(
        self,
        entity,
    ):
        self.session.delete(entity)

    def commit(self):
        self.session.commit()

    def flush(self):
        self.session.flush()