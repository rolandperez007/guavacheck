from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.session import get_db
from app.security.authentication import get_current_user
from app.users.models.user import User


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/me")
def get_me(
    current_user_id: str = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    user = (
        db.query(User)
        .filter(User.id == current_user_id)
        .first()
    )

    if not user:
        from fastapi import HTTPException

        raise HTTPException(
            status_code=401,
            detail="User no longer exists",
        )

    return {
        "id": user.id,
        "email": user.email,
        "username": user.username,
        "identity_id": user.identity_id,
        "role": user.role,
        "status": user.status,
        "active": user.active,
        "verified": user.verified,
    }