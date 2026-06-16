from fastapi import APIRouter
from pydantic import BaseModel
from app.core.austin_parser import AustinParser
from app.core.austin_brain import AustinBrain
from app.core.austin_ai_gateway import AustinAIGateway
from app.core.austin_orchestrator import AustinOrchestrator
from app.core.austin_memory import AustinMemory
from fastapi import APIRouter


router = APIRouter()

parser = AustinParser()
brain = AustinBrain()

memory = AustinMemory()
orchestrator = AustinOrchestrator(memory_store=memory)

class AustinRequest(BaseModel):
    user_id: str
    query: str
    action: str = "analyze"


@router.post("/execute")
def execute(req: AustinRequest):

    parsed = parser.parse(req.query)
    analysis = brain.analyze(parsed)

    result = orchestrator.execute(
        user_id=req.user_id,
        query=req.query,
        analysis=analysis
    )

    memory.save(req.user_id, result)
    history = memory.get_history(req.user_id)

    result["history"] = history[-5:]

    return result

    explanation = gpt.reason(req.user_id, req.query, analysis)

    event = {
        "user_id": req.user_id,
        "query": req.query,
        "analysis": analysis,
        "explanation": explanation
    }

    memory.save(req.user_id, event)
    history = memory.get_history(req.user_id)
    
    if analysis.get("score", 0) < 0.3:
        explanation = gpt._offline_reason(req.query, analysis)
    else:
        explanation = gpt.reason(req.query, analysis) 
    
    return {
        "status": "success",
        "analysis": analysis,
        "explanation": explanation,
        "history": history[-5:]
    }