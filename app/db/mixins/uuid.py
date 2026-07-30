from uuid import uuid4

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db.constants import UUID_LENGTH


class UUIDMixin:
    """
    Adds a UUID primary key to a model.
    """

    id: Mapped[str] = mapped_column(
        String(UUID_LENGTH),
        primary_key=True,
        default=lambda: str(uuid4()),
    )