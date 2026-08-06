from __future__ import annotations

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.db.mixins import TimestampMixin
from app.db.mixins import UUIDMixin


class Workflow(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    """
    Persisted workflow definition.
    """

    __tablename__ = "workflows"

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
        index=True,
    )

    version: Mapped[str] = mapped_column(
        String(20),
        default="1.0",
    )

    description: Mapped[str | None] = mapped_column(
        String(1000),
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="active",
    )

    nodes = relationship(
        "WorkflowNodeModel",
        back_populates="workflow",
        cascade="all, delete-orphan",
    )

    edges = relationship(
        "WorkflowEdgeModel",
        back_populates="workflow",
        cascade="all, delete-orphan",
    )

    executions = relationship(
        "WorkflowExecution",
        back_populates="workflow",
        cascade="all, delete-orphan",
    )