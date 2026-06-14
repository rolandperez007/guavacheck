class EvaluationEngine:
    def evaluate(self, query: str, model: str, response):
        return {"query": query, "model": model, "status": "logged"}
