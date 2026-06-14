class AgentBase:
    """
    Base contract for all swarm agents
    """

    name = "base"

    async def run(self, query: str):
        raise NotImplementedError("Agent must implement run()")
