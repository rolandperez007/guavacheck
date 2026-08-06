"""
World Bootstrap

Starts the World Runtime,
loads world intelligence,
and builds the world graph.
"""


from app.world.data import WorldSeeder

from app.world.graph import WorldGraphRuntime



class WorldBootstrap:


    def __init__(
        self,
        runtime,
        registry,
        seeder=None,
        graph=None,
    ):

        self.runtime = runtime

        self.registry = registry

        self.seeder = seeder or WorldSeeder(
            registry
        )

        self.graph = graph or WorldGraphRuntime()



    def boot(self):


        world_state = self.seeder.seed()


        entities = []


        for country in self.registry.countries.values():

            entities.append(
                country
            )


        for district in self.registry.districts.values():

            entities.append(
                district
            )


        self.graph.load(
            entities
        )


        self.runtime.status = "running"


        return {

            "status": "online",

            "world": world_state,

            "graph": {

                "relationships": len(
                    self.graph.relationships
                )

            }

        }