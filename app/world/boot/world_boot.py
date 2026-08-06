"""
World Boot Manager

Responsible for starting the complete World Runtime.
"""


from app.world.kernel.kernel_state import KernelState


class WorldBootManager:


    def __init__(
        self,
        kernel,
        loader=None,
        registry=None,
    ):

        self.kernel = kernel
        self.loader = loader
        self.registry = registry

        self.state = KernelState()


    def boot(self):

        result = self.kernel.boot()

        self.state.status = "running"


        if self.registry:

            self.state.countries_loaded = len(
                self.registry.countries
            )

            self.state.districts_loaded = len(
                self.registry.districts
            )

            self.state.engines_connected = len(
                self.registry.engines
            )


        return {

            "world_kernel": result,

            "state": self.state,

        }