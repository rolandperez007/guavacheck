from sqlalchemy.orm import Session

from app.vision.models.project import VisionProject


class ProjectRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, project: VisionProject):

        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)

        return project

    def get(self, project_id: str):

        return (
            self.db.query(VisionProject).filter(VisionProject.id == project_id).first()
        )

    def list(self):

        return self.db.query(VisionProject).all()

    def delete(self, project_id: str):

        project = self.get(project_id)

        if project:
            self.db.delete(project)
            self.db.commit()
