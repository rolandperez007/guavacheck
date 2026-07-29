from sqlalchemy.orm import Session

from app.twin.models import Twin


class TwinRepository:

    @staticmethod
    def create(
        db: Session,
        twin: Twin,
    ):
        db.add(twin)
        db.commit()
        db.refresh(twin)
        return twin

    @staticmethod
    def get(
        db: Session,
        twin_id: str,
    ):
        return (
            db.query(Twin)
            .filter(Twin.id == twin_id)
            .first()
        )

    @staticmethod
    def list(
        db: Session,
    ):
        return db.query(Twin).all()