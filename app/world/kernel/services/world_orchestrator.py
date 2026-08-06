class WorldOrchestrator:


    def __init__(
        self,
        kernel,
    ):
        self.kernel = kernel


    def execute(
        self,
        request,
    ):

        return self.kernel.resolve_location(
            country=request.get("country"),
            district=request.get("district"),
        )