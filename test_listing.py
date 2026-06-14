import asyncio

from app.agents.listing_agent import ListingAgent


async def main():
    agent = ListingAgent()

    result = await agent.run("show me properties in lekki")

    print(result)


asyncio.run(main())
