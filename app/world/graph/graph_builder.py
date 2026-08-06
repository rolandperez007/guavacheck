"""
World Graph Builder

Creates relationships between
world entities.
"""


from app.world.graph.relationship import Relationship



class WorldGraphBuilder:


    def __init__(
        self,
    ):

        self.relationships = []



    def add_relationship(
        self,
        source,
        relation,
        target,
    ):


        relationship = Relationship(

            source,

            relation,

            target,

        )


        self.relationships.append(
            relationship
        )


        return relationship



    def build_country_tree(
        self,
    ):


        self.add_relationship(

            "West Africa",

            "INCLUDES",

            "Nigeria",

        )


        self.add_relationship(

            "Nigeria",

            "CONTAINS",

            "Lagos",

        )


        self.add_relationship(

            "Lagos",

            "CONTAINS",

            "Victoria Island",

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