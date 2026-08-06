from sqlalchemy.orm import Session

from app.vision.models.project import VisionProject
from app.vision.models.render import Render
from app.vision.models.room import Room
from app.vision.prompts.interior_prompt import InteriorPromptBuilder
from app.vision.providers.provider_factory import ProviderFactory
from app.vision.repositories.project_repository import ProjectRepository
from app.vision.repositories.render_repository import RenderRepository
from app.vision.repositories.room_repository import RoomRepository


class VisionService:
    def __init__(self, db: Session):
        self.db = db

        self.projects = ProjectRepository(db)
        self.rooms = RoomRepository(db)
        self.renders = RenderRepository(db)

    # ==========================================================
    # PROJECTS
    # ==========================================================

    def create_project(self, project: VisionProject):
        return self.projects.create(project)

    def create_project_from_schema(self, payload):

        project = VisionProject(
            name=payload.name,
            owner_id=payload.owner_id,
            property_type=payload.property_type,
            design_style=payload.design_style,
            budget=payload.budget,
            location=payload.location,
        )

        return self.projects.create(project)

    def get_project(self, project_id: str):
        return self.projects.get(project_id)

    def list_projects(self):
        return self.projects.list()

    # ==========================================================
    # ROOMS
    # ==========================================================

    def create_room(self, room: Room):
        return self.rooms.create(room)

    def project_rooms(self, project_id: str):
        return self.rooms.by_project(project_id)

    # ==========================================================
    # RENDERS
    # ==========================================================

    def save_render(self, render: Render):
        return self.renders.create(render)

    def room_renders(self, room_id: str):
        return self.renders.by_room(room_id)

    # ==========================================================
    # AI
    # ==========================================================

    def generate_interior(
        self,
        project_id: str,
        room_id: str,
        provider_name: str = "openai",
    ):

        project = self.projects.get(project_id)

        if project is None:
            raise ValueError("Project not found.")

        room = self.rooms.get(room_id)

        if room is None:
            raise ValueError("Room not found.")

        prompt = InteriorPromptBuilder.build(
            project,
            room,
        )

        provider = ProviderFactory.get(
            provider_name,
        )

        image = provider.generate_interior(
            prompt,
        )

        return image

    def update_project(self, project_id: str, payload):

        project = self.projects.get(project_id)

        if project is None:
            return None

        if payload.name is not None:
            project.name = payload.name

        if payload.design_style is not None:
            project.design_style = payload.design_style

        if payload.budget is not None:
            project.budget = payload.budget

        if payload.location is not None:
            project.location = payload.location

        if payload.status is not None:
            project.status = payload.status

        self.projects.update()

        return project

    def delete_project(self, project_id: str):

        project = self.projects.get(project_id)

        if project is None:
            return False

        self.projects.delete(project)

        return True
