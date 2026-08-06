from __future__ import annotations

from sqlalchemy.orm import Session

from app.institution.models.offer import Offer
from app.institution.repositories.base_repository import BaseRepository


class OfferRepository(BaseRepository[Offer]):
    """
    Repository for Product Offers.
    """

    def __init__(self, db: Session):
        super().__init__(db)

    def get(
        self,
        offer_id: str,
    ) -> Offer | None:
        return (
            self.db.query(Offer)
            .filter(Offer.id == offer_id)
            .first()
        )

    def list_by_product(
        self,
        product_id: str,
    ) -> list[Offer]:
        return (
            self.db.query(Offer)
            .filter(
                Offer.product_id == product_id
            )
            .all()
        )