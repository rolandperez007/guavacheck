from datetime import datetime


class CostTracker:
    def log(self, model: str, score: float, prompt: str):
        print(
            {
                "timestamp": datetime.utcnow().isoformat(),
                "model": model,
                "score": score,
                "tokens_estimate": len(prompt.split()),
            }
        )
