from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.vision.models.base import VisionBase


class Render(VisionBase):
    __tablename__ = "vision_renders"

    project_id: Mapped[str] = mapped_column(
        ForeignKey("vision_projects.id"),
        nullable=False,
    )

    room_id: Mapped[str] = mapped_column(
        ForeignKey("vision_rooms.id"),
        nullable=False,
    )

    image_url: Mapped[str] = mapped_column(
        String(500),
        nullable=True,
    )

    provider: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    prompt: Mapped[str] = mapped_column(
        String(4000),
        nullable=True,
    )

    version: Mapped[int] = mapped_column(
        Integer,
        default=1,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="pending",
    )

    project = relationship(
        "VisionProject",
        back_populates="renders",
    )

    room = relationship(
        "Room",
        back_populates="renders",
    )