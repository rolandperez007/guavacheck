"""
World Bootstrap

Starts the World Runtime
and loads world intelligence.
"""


from app.world.data import WorldSeeder



class WorldBootstrap:


    def __init__(
        self,
        runtime,
        registry,
        seeder=None,
    ):

        self.runtime = runtime

        self.registry = registry

        self.seeder = seeder or WorldSeeder(
            registry
        )



    def boot(self):


        world_state = self.seeder.seed()


        self.runtime.status = "running"


        return {

            "status": "online",

            "world": world_state,

        }