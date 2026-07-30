from sqlalchemy import ForeignKey
from sqlalchemy import Float
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

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