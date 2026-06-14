from fastapi import APIRouter
from app.agents.listing_agent import ListingAgent
from app.agents.swarm.swarm_v2 import SwarmV2

router = APIRouter()

agent = ListingAgent()
swarm = SwarmV2()


@router.get("/austin")
async def austin(query: str):
    result = await agent.run(query)

    swarm_result = swarm.run(query, result.get("routing"))

    return {"austin": result, "swarm": swarm_result}
