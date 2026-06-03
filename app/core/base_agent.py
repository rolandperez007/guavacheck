class BaseAgent:

    def __init__(self, services=None):
        self.services = services or {}

    async def run(self, query: str):
        raise NotImplementedError