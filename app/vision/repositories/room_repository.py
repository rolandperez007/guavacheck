from sqlalchemy.orm import Session

from app.vision.models.room import Room
from app.vision.repositories.base import BaseRepository


class RoomRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db)

    def create(self, room: Room):
        return self.add(room)

    def by_project(self, project_id: str):
        return self.db.query(Room).filter(Room.project_id == project_id).all()

    def get(self, room_id: str):
        return self.db.query(Room).filter(Room.id == room_id).first()
