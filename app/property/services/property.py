from sqlalchemy.orm import Session

from app.property.repositories.property import PropertyRepository
from app.property.schemas.property import PropertyCreate


class PropertyService:
    def __init__(self):

        self.repository = PropertyRepository()

    def create_property(self, db: Session, data: PropertyCreate):

        existing = self.repository.get_by_reference(db, data.reference_code)

        if existing:
            raise ValueError("Property reference already exists")

        return self.repository.create(db, data)

    def get_property(self, db: Session, property_id: str):

        return self.repository.get_by_id(db, property_id)
