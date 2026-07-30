from sqlalchemy import ForeignKey
from sqlalchemy import Float
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.vision.models.base import VisionBase


class Room(VisionBase):
    __tablename__ = "vision_rooms"

    project_id: Mapped[str] = mapped_column(
        ForeignKey("vision_projects.id"),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    room_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    width: Mapped[float] = mapped_column(
        Float,
        nullable=True,
    )

    length: Mapped[float] = mapped_column(
        Float,
        nullable=True,
    )

    height: Mapped[float] = mapped_column(
        Float,
        nullable=True,
    )

    project = relationship(
        "VisionProject",
        back_populates="rooms",
    )

    renders = relationship(
        "Render",
        back_populates="room",
        cascade="all, delete-orphan",
    )