from __future__ import annotations

from sqlalchemy.orm import Session


class UnitOfWork:
    """
    Lightweight transaction boundary for service-layer orchestration.

    This keeps the repository/service pattern consistent without forcing
    a framework-specific transaction manager into the module.
    """

    def __init__(self, db: Session):
        self.db = db

    def commit(self) -> None:
        self.db.commit()

    def rollback(self) -> None:
        self.db.rollback()

    def flush(self) -> None:
        self.db.flush()
