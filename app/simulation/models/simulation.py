from __future__ import annotations

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.db.mixins import TimestampMixin
from app.db.mixins import UUIDMixin


class Simulation(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    """
    Root simulation aggregate.
    """

    __tablename__ = "simulations"

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )

    engine: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="draft",
    )

    executions = relationship(
        "SimulationExecution",
        back_populates="simulation",
        cascade="all, delete-orphan",
    )

    scenarios = relationship(
        "Scenario",
        back_populates="simulation",
        cascade="all, delete-orphan",
    )

    reports = relationship(
        "SimulationReportModel",
        back_populates="simulation",
        cascade="all, delete-orphan",
    )