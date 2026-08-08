from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.auth.schemas.login import LoginRequest
from app.auth.schemas.token import TokenResponse

from app.auth.services.auth_service import AuthService



router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


service = AuthService()



@router.get("/")
def auth_status():

    return {
        "module": "authentication",
        "status": "active"
    }



@router.post("/login", response_model=TokenResponse)
def login(
    data: LoginRequest,
    db: Session = Depends(get_db)
):

    result = service.login(
        db,
        data.email,
        data.password
    )


    if not result:

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )


    return result