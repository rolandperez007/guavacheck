from typing import Any


class AustinBrainV2:
    """
    Intelligent tool routing brain (GPT-style decision layer)
    """

    def __init__(self):
        self.tools = {
            "listing": [
                "buy",
                "rent",
                "property",
                "house",
                "apartment",
                "lekki",
                "land",
            ],
            "pricing": ["price", "cost", "valuation", "worth", "estimate"],
            "mortgage": [
                "loan",
                "mortgage",
                "interest",
                "repayment",
                "monthly payment",
            ],
            "roi": ["roi", "return", "investment", "profit", "yield"],
            "market": ["market", "trend", "demand", "area", "growth"],
        }

    def _score_tool(self, query: str, keywords: list[str]) -> float:
        query = query.lower()
        score = 0

        for kw in keywords:
            if kw in query:
                score += 1

        # normalize confidence
        return min(score / max(len(keywords), 1), 1.0)

    def route(self, query: str) -> dict[str, Any]:
        scores = {}

        for tool, keywords in self.tools.items():
            scores[tool] = self._score_tool(query, keywords)

        # pick best match
        best_tool = max(scores, key=scores.get)
        best_score = scores[best_tool]

        # fallback logic
        if best_score < 0.2:
            return {
                "tool": "listing",
                "confidence": 0.3,
                "reason": "fallback default route",
            }

        return {
            "tool": best_tool,
            "confidence": round(best_score, 2),
            "reason": "semantic match",
        }
