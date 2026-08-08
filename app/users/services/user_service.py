from sqlalchemy.orm import Session

from app.users.models.user import User
from app.users.repositories.user_repository import UserRepository
from app.users.schemas.user import UserCreate


class UserService:


    def __init__(self):

        self.repository = UserRepository()



    def create_user(
        self,
        db: Session,
        data: UserCreate
    ):

        existing = (
            self.repository
            .get_by_identity(
                db,
                data.identity_id
            )
        )


        if existing:

            return existing



        user = User(
            identity_id=data.identity_id,
            username=data.username,
            password_hash=data.password
        )


        return (
            self.repository
            .create(
                db,
                user
            )
        )