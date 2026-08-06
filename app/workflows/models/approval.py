from __future__ import annotations

from sqlalchemy import Boolean
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db.base import Base
from app.db.mixins import TimestampMixin
from app.db.mixins import UUIDMixin


class WorkflowApprovalModel(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    """
    Human approval configuration.
    """

    __tablename__ = "workflow_approvals"

    role: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    required: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    approved: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )