"""
World Graph Auto Builder

Builds relationships automatically
from world entity data.
"""


from app.world.graph.relationship import Relationship



class AutoGraphBuilder:


    def __init__(
        self,
    ):

        self.relationships = []



    def build_from_entity(
        self,
        entity,
    ):


        name = entity.get(
            "name"
        )


        parent = entity.get(
            "parent"
        )


        if parent:


            relationship = Relationship(

                parent,

                "CONTAINS",

                name,

            )


            self.relationships.append(
                relationship
            )


        return self.relationships



    def build(
        self,
        entities,
    ):


        for entity in entities:

            self.build_from_entity(
                entity
            )


        return self.relationships



    def export(
        self,
    ):


        return [

            relationship.to_dict()

            for relationship

            in self.relationships

        ]