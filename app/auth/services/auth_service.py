from sqlalchemy.orm import Session

from app.auth.repositories.auth_repository import AuthRepository
from app.security.password import verify_password
from app.auth.services.token_service import create_access_token


class AuthService:


    def __init__(self):

        self.repository = AuthRepository()



    def login(
        self,
        db: Session,
        email: str,
        password: str
    ):

        user = (
            self.repository
            .get_user_by_email(
                db,
                email
            )
        )


        if not user:

            return None


        valid = verify_password(
            password,
            user.password_hash
        )


        if not valid:

            return None


        token = create_access_token(
            user.id
        )


        return {

            "access_token": token,

            "token_type": "bearer"

        }