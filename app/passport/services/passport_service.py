from datetime import datetime
from uuid import uuid4

from app.passport.models.passport import PropertyPassport
from app.passport.repository.passport_repository import PassportRepository
from app.passport.schemas.passport import PropertyPassportCreate


class PassportService:

    def __init__(self):

        self.repository = PassportRepository()

    def _generate_passport_id(self) -> str:

        return f"GC-PAS-{uuid4().hex[:8].upper()}"

    def _generate_asset_uid(
        self,
        property_type: str,
        country: str,
        state: str,
    ) -> str:

        property_code = property_type[:3].upper()

        country_code = country[:3].upper()

        state_code = state[:3].upper()

        unique = uuid4().hex[:8].upper()

        return f"GVA-{property_code}-{country_code}-{state_code}-{unique}"

    def create(
        self,
        request: PropertyPassportCreate,
    ) -> PropertyPassport:

        passport = PropertyPassport(

            passport_id=self._generate_passport_id(),

            asset_uid=self._generate_asset_uid(
                request.property_type,
                request.country,
                request.state,
            ),

            property_name=request.property_name,

            property_type=request.property_type,

            owner_id=request.owner_id,

            country=request.country,

            state=request.state,

            city=request.city,

            address=request.address,

            latitude=request.latitude,

            longitude=request.longitude,

            construction_year=request.construction_year,

            land_area=request.land_area,

            building_area=request.building_area,

            verified=False,

            dna_generated=False,

            twin_generated=False,

            published=False,

            created_at=datetime.utcnow(),

            updated_at=datetime.utcnow(),
        )

        self.repository.create(passport)

        return passport

    def get(
        self,
        passport_id: str,
    ):

        return self.repository.get(passport_id)

    def list(self):

        return self.repository.list()

    def update(
        self,
        passport_id: str,
        request,
    ):

        return self.repository.update(
            passport_id,
            request,
        )

    def delete(
        self,
        passport_id: str,
    ):

        return self.repository.delete(
            passport_id,
        )