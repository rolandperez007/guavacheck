from __future__ import annotations

from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.db.mixins import TimestampMixin
from app.db.mixins import UUIDMixin


class WorkflowNodeModel(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    """
    Stored workflow node.
    """

    __tablename__ = "workflow_nodes"

    workflow_id: Mapped[UUID] = mapped_column(
        ForeignKey("workflows.id"),
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    node_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    workflow = relationship(
        "Workflow",
        back_populates="nodes",
    )