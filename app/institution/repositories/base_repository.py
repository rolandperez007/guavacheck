from __future__ import annotations

from typing import Generic
from typing import TypeVar

from sqlalchemy.orm import Session

T = TypeVar("T")


class BaseRepository(Generic[T]):
    """
    Base repository for the Institution module.

    Repositories never commit transactions.
    """

    def __init__(self, db: Session):
        self.db = db

    def add(self, entity: T) -> T:
        self.db.add(entity)
        return entity

    def delete(self, entity: T) -> None:
        self.db.delete(entity)

    def flush(self) -> None:
        self.db.flush()

    def refresh(self, entity: T) -> None:
        self.db.refresh(entity)