from sqlalchemy.orm import Session

from app.identity.models.identity import Identity
from app.users.models.user import User


class AuthRepository:


    def get_user_by_email(
        self,
        db: Session,
        email: str
    ):

        return (
            db.query(User)
            .join(
                Identity,
                User.identity_id == Identity.id
            )
            .filter(
                Identity.email == email
            )
            .first()
        )