from sqlalchemy.orm import Session

from app.identity.models.identity import Identity
from app.security.password import hash_password
from app.users.models.user import User
from app.users.schemas.register import RegisterRequest


class RegistrationService:

    def register(
        self,
        db: Session,
        data: RegisterRequest,
    ) -> User:

        # Prevent duplicate usernames.
        existing_username = (
            db.query(User)
            .filter(User.username == data.username)
            .first()
        )

        if existing_username:
            raise ValueError("Username already exists")

        # Prevent duplicate identities/emails.
        existing_identity = (
            db.query(Identity)
            .filter(Identity.email == data.email)
            .first()
        )

        if existing_identity:
            raise ValueError("Email already exists")

        try:
            # Create the identity first so its generated ID
            # can be assigned to the User.
            identity = Identity(
                email=data.email,
                status="active",
                identity_type="individual",
            )

            db.add(identity)
            db.flush()

            # Create the application user.
            user = User(
                identity_id=identity.id,
                username=data.username,
                email=data.email,
                password_hash=hash_password(data.password),
                first_name="",
                last_name="",
                role="user",
                active=True,
                verified=False,
                status="active",
            )

            db.add(user)
            db.flush()

            # Commit Identity + User together.
            db.commit()

            # Refresh the persisted User.
            db.refresh(user)

            return user

        except Exception:
            db.rollback()
            raise