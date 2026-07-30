from sqlalchemy.orm import Session

from app.vision.models.render import Render
from app.vision.repositories.base import BaseRepository


class RenderRepository(BaseRepository):

    def __init__(self, db: Session):
        super().__init__(db)

    def create(self, render: Render):
        return self.add(render)

    def by_room(self, room_id: str):
        return (
            self.db.query(Render)
            .filter(Render.room_id == room_id)
            .order_by(Render.version.desc())
            .all()
        )

    def get(self, render_id: str):
        return (
            self.db.query(Render)
            .filter(Render.id == render_id)
            .first()
        )