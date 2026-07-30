from sqlalchemy import ForeignKey
from sqlalchemy import Float
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.vision.models.base import VisionBase


class Furniture(VisionBase):
    __tablename__ = "vision_furniture"

    room_id: Mapped[str] = mapped_column(
        ForeignKey("vision_rooms.id"),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    category: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    quantity: Mapped[float] = mapped_column(
        Float,
        default=1,
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