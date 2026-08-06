from sqlalchemy import Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.vision.models.base import VisionBase


class Material(VisionBase):
    __tablename__ = "vision_materials"

    room_id: Mapped[str] = mapped_column(
        ForeignKey("vision_rooms.id"),
        nullable=False,
    )

    category: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    unit: Mapped[str] = mapped_column(
        String(20),
        nullable=True,
    )

    quantity: Mapped[float] = mapped_column(
        Float,
        nullable=True,
    )

    estimated_cost: Mapped[float] = mapped_column(
        Float,
        nullable=True,
    )

    supplier: Mapped[str] = mapped_column(
        String(200),
        nullable=True,
    )

    room = relationship("Room")
