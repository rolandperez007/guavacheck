"""
World Relationship Model

Defines connections between
world entities.
"""



class Relationship:


    def __init__(
        self,
        source,
        relation,
        target,
    ):

        self.source = source

        self.relation = relation

        self.target = target



    def to_dict(
        self,
    ):

        return {

            "source": self.source,

            "relation": self.relation,

            "target": self.target,

        }