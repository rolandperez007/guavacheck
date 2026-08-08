from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.identity.models.identity import Identity
from app.security.authentication import get_current_user
from app.users.models.user import User


def get_authenticated_user(
    user_id: str = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> User:
    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User no longer exists",
        )

    if not user.active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is inactive",
        )

    if user.status != "active":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is not active",
        )

    return user


def get_authenticated_identity(
    user: User = Depends(get_authenticated_user),
    db: Session = Depends(get_db),
) -> Identity:
    identity = (
        db.query(Identity)
        .filter(Identity.id == user.identity_id)
        .first()
    )

    if not identity:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User identity no longer exists",
        )

    if identity.status != "active":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Identity is not active",
        )

    return identity