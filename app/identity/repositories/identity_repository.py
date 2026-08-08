from sqlalchemy.orm import Session

from app.identity.models.identity import Identity


class IdentityRepository:


    def create(
        self,
        db: Session,
        identity: Identity
    ):

        db.add(identity)

        db.commit()

        db.refresh(identity)

        return identity


    def get_by_email(
        self,
        db: Session,
        email: str
    ):

        return (
            db.query(Identity)
            .filter(
                Identity.email == email
            )
            .first()
        )