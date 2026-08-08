from __future__ import annotations

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.db.constants import UUID_LENGTH
from app.db.mixins import TimestampMixin


class ProductService(
    TimestampMixin,
    Base,
):
    """
    Associates Products with Services.

    Example:

    Mortgage Product
        ├── Property Valuation
        ├── Legal Review
        ├── Survey
        └── Insurance
    """

    __tablename__ = "institution_product_services"

    product_id: Mapped[str] = mapped_column(
        String(UUID_LENGTH),
        ForeignKey(
            "institution_products.id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )

    service_id: Mapped[str] = mapped_column(
        String(UUID_LENGTH),
        ForeignKey(
            "institution_services.id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )
