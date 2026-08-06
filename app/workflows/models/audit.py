from __future__ import annotations

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db.base import Base
from app.db.mixins import TimestampMixin
from app.db.mixins import UUIDMixin


class WorkflowAudit(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    """
    Audit trail for workflow events.
    """

    __tablename__ = "workflow_audit"

    event: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    actor: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    details: Mapped[str | None] = mapped_column(
        String(2000),
    )