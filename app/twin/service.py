from app.twin.models import Twin
from app.twin.repository import TwinRepository


class TwinService:
    @staticmethod
    def create(
        db,
        request,
    ):

        twin = Twin(
            property_id=request.property_id,
            owner_id=request.owner_id,
        )

        return TwinRepository.create(
            db,
            twin,
        )
