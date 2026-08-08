from sqlalchemy.orm import Session

from app.identity.models.identity import Identity
from app.identity.repositories.identity_repository import IdentityRepository
from app.identity.schemas.identity import IdentityCreate


class IdentityService:


    def __init__(self):

        self.repository = IdentityRepository()


    def create_identity(
        self,
        db: Session,
        data: IdentityCreate
    ):

        existing = (
            self.repository
            .get_by_email(
                db,
                data.email
            )
        )

        if existing:

            return existing


        identity = Identity(
            email=data.email,
            phone=data.phone,
            identity_type=data.identity_type
        )


        return (
            self.repository
            .create(
                db,
                identity
            )
        )