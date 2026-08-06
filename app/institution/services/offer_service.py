from __future__ import annotations

from sqlalchemy.orm import Session

from app.institution.models.offer import Offer
from app.institution.repositories.offer_repository import (
    OfferRepository,
)
from app.institution.services.base_service import BaseService


class OfferService(BaseService):

    def __init__(
        self,
        db: Session,
    ):
        super().__init__(db)

        self.offers = OfferRepository(db)

    def create(
        self,
        offer: Offer,
    ) -> Offer:

        self.offers.add(offer)

        self.commit()

        self.db.refresh(offer)

        return offer

    def get(
        self,
        offer_id: str,
    ) -> Offer | None:
        return self.offers.get(offer_id)

    def list_by_product(
        self,
        product_id: str,
    ) -> list[Offer]:
        return self.offers.list_by_product(
            product_id,
        )