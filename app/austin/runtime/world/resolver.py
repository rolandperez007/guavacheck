"""
Austin World Resolver

Connects Austin's cognitive runtime
to World OS entities.
"""


class WorldResolver:


    def __init__(
        self,
        registry=None,
        graph=None,
    ):

        self.registry = registry

        self.graph = graph



    def resolve(
        self,
        name,
    ):


        result = {

            "entity": name,

            "type": "unknown",

        }


        if self.registry:


            if name in self.registry.countries:


                result["type"] = "country"



            elif name in self.registry.districts:


                result["type"] = "district"



        return result