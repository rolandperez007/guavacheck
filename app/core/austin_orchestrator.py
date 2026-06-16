from app.core.austin_parser import AustinParser
from app.core.austin_brain import AustinBrain
from app.core.austin_ai_gateway import AustinAIGateway


class AustinOrchestrator:

    def __init__(self, memory_store=None):
        self.memory = memory_store
        self.parser = AustinParser()
        self.brain = AustinBrain()
        self.gpt = AustinAIGateway()

    def run(self, user_id: str, query: str):

        parsed = self.parser.parse(query)
        analysis = self.brain.analyze(parsed)

        # decision layer
        if analysis.get("confidence", 0) < 0.4:
            response = self.gpt.reason(query, analysis)
        else:
            response = self.brain.reason(query, analysis)

        return {
            "user_id": user_id,
            "query": query,
            "parsed": parsed,
            "analysis": analysis,
            "response": response
        }