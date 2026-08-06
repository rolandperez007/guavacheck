"""
World Bootstrap

Connects runtime components.
"""


class WorldBootstrap:


    def __init__(
        self,
        runtime,
        registry,
    ):

        self.runtime = runtime

        self.registry = registry



    def boot(self):

        self.runtime.status = "running"


        return {

            "status": "online",

            "registry": self.registry.summary(),

        }