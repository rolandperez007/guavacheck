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


class Scenario(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    """
    Persisted scenario template.
    """

    __tablename__ = "simulation_scenarios"

    simulation_id: Mapped[UUID] = mapped_column(
        ForeignKey("simulations.id"),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    version: Mapped[str] = mapped_column(
        String(20),
        default="1.0",
    )

    simulation = relationship(
        "Simulation",
        back_populates="scenarios",
    )