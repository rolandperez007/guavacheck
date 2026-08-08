from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database.session import get_db


router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get("/database")
def database_health(
    db: Session = Depends(get_db)
):

    try:

        db.execute(
            text("SELECT 1")
        )

        return {
            "database": "connected",
            "status": "healthy"
        }

    except Exception as error:

        return {
            "database": "unavailable",
            "status": "error",
            "detail": str(error)
        }