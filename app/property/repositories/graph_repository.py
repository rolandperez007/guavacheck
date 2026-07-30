from app.property.repositories.registry import RepositoryRegistry
from app.property.schemas.graph import PropertyGraph


class PropertyGraphRepository:

    def __init__(self):

        self.repositories = RepositoryRegistry()

    def load(self, property_id: str) -> PropertyGraph:

        property_data = self.repositories.property.get(property_id)

        #
        # These become active as the repositories are connected.
        #

        passport = None
        twin = None
        vision_projects = []
        knowledge = []
        images = []
        engineering = []
        versions = []

        return PropertyGraph(
            property=property_data.model_dump()
            if hasattr(property_data, "model_dump")
            else property_data,
            passport=passport,
            twin=twin,
            vision_projects=vision_projects,
            knowledge=knowledge,
            images=images,
            engineering_snapshots=engineering,
            versions=versions,
        )