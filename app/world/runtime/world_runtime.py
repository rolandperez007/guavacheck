"""
World Runtime

High level coordinator for:

Templates
Loader
Registry
Kernel
"""


class WorldRuntime:


    def __init__(
        self,
        kernel,
        registry,
        loader=None,
        templates=None,
    ):

        self.kernel = kernel
        self.registry = registry
        self.loader = loader
        self.templates = templates


        self.status = "created"



    def start(self):

        self.status = "running"


        return {

            "runtime": "world",

            "status": self.status,

            "kernel": self.kernel.status,

        }