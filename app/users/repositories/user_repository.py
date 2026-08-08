from sqlalchemy.orm import Session

from app.users.models.user import User


class UserRepository:


    def create(
        self,
        db: Session,
        user: User
    ):

        db.add(user)

        db.commit()

        db.refresh(user)

        return user



    def get_by_identity(
        self,
        db: Session,
        identity_id: str
    ):

        return (
            db.query(User)
            .filter(
                User.identity_id == identity_id
            )
            .first()
        )