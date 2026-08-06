from __future__ import annotations

from sqlalchemy.orm import Session

from app.db.unit_of_work import UnitOfWork


class BaseService:
    """
    Base service for the Institution module.

    Services coordinate business logic and transactions.
    """

    def __init__(
        self,
        db: Session,
    ):
        self.db = db
        self.uow = UnitOfWork(db)

    def commit(self) -> None:
        """
        Commit the current transaction.
        """
        self.uow.commit()

    def rollback(self) -> None:
        """
        Roll back the current transaction.
        """
        self.uow.rollback()

    def flush(self) -> None:
        """
        Flush pending changes to the database.
        """
        self.uow.flush()