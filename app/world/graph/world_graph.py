"""
World Graph Runtime

Provides navigation and querying
over the world relationship graph.
"""


from app.world.graph import AutoGraphBuilder



class WorldGraphRuntime:


    def __init__(
        self,
    ):

        self.entities = []

        self.relationships = []



    def load(
        self,
        entities,
    ):

        self.entities = entities


        builder = AutoGraphBuilder()


        relationships = builder.build(
            entities
        )


        self.relationships = relationships


        return self.relationships



    def find_children(
        self,
        entity,
    ):


        results = []


        for relationship in self.relationships:


            if (
                relationship.source
                ==
                entity
                and
                relationship.relation
                ==
                "CONTAINS"
            ):

                results.append(
                    relationship.target
                )


        return results



    def find_parent(
        self,
        entity,
    ):


        for relationship in self.relationships:


            if (
                relationship.target
                ==
                entity
                and
                relationship.relation
                ==
                "CONTAINS"
            ):

                return relationship.source


        return None



    def export(
        self,
    ):


        return [

            relationship.to_dict()

            for relationship

            in self.relationships

        ]