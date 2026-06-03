class SwarmCoordinator:

    def __init__(self, agents):
        self.agents = agents

    async def run(self, query: str):

        tasks = []

        # parallel thinking
        for name, agent in self.agents.items():
            tasks.append(agent.run(query))

        results = await self._gather(tasks)

        return {
            "query": query,
            "agents_used": list(self.agents.keys()),
            "results": results
        }

    async def _gather(self, tasks):
        import asyncio
        return await asyncio.gather(*tasks)