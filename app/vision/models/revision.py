from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.vision.models.base import VisionBase


class DesignRevision(VisionBase):
    __tablename__ = "vision_revisions"

    render_id: Mapped[str] = mapped_column(
        ForeignKey("vision_renders.id"),
        nullable=False,
    )

    revision_number: Mapped[int] = mapped_column(
        Integer,
        default=1,
    )

    notes: Mapped[str] = mapped_column(
        String(1000),
        nullable=True,
    )

    image_url: Mapped[str] = mapped_column(
        String(500),
        nullable=True,
    )

    render = relationship("Render")