from __future__ import annotations

from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.db.mixins import TimestampMixin
from app.db.mixins import UUIDMixin


class WorkflowExecution(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    """
    Workflow execution history.
    """

    __tablename__ = "workflow_executions"

    workflow_id: Mapped[UUID] = mapped_column(
        ForeignKey("workflows.id"),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="queued",
    )

    duration_ms: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    workflow = relationship(
        "Workflow",
        back_populates="executions",
    )