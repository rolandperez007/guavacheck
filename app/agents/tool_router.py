import os
import numpy as np
from openai import OpenAI


class ToolRouter:
    """
    GPT-level Tool Router (Semantic Decision Engine)

    - Uses embeddings instead of keywords
    - Chooses best tool by cosine similarity
    """

    def __init__(self, tools=None):
        self.tools = tools or {}
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        # Tool descriptions = brain anchors
        self.tool_map = {
            "listing": "Find properties, houses, apartments, rentals, real estate listings in locations like Lekki, Lagos, Abuja",
            "pricing": "Estimate property prices, cost analysis, budget calculations for real estate",
            "insight": "Market trends, real estate analytics, investment insights, forecasting"
        }

        self.tool_embeddings = self._build_tool_embeddings()

    # -----------------------------
    # EMBEDDING
    # -----------------------------
    def _embed(self, text: str):
        response = self.client.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )
        return np.array(response.data[0].embedding)

    # -----------------------------
    # BUILD TOOL SPACE
    # -----------------------------
    def _build_tool_embeddings(self):
        embeddings = {}
        for tool, desc in self.tool_map.items():
            embeddings[tool] = self._embed(desc)
        return embeddings

    # -----------------------------
    # COSINE SIMILARITY
    # -----------------------------
    def _similarity(self, a, b):
        return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

    # -----------------------------
    # ROUTE QUERY
    # -----------------------------
    def route(self, query, memory=None):
        query_vec = self._embed(query)

        scores = {}

        for tool, vec in self.tool_embeddings.items():
            scores[tool] = self._similarity(query_vec, vec)

        best_tool = max(scores, key=scores.get)
        confidence = scores[best_tool]

        reason = f"semantic match to {best_tool}"

        # MEMORY BOOST (optional enhancement)
        if memory and memory.get("locations"):
            for loc in memory["locations"]:
                if loc.lower() in query.lower():
                    confidence = min(confidence + 0.08, 0.99)
                    reason += " + memory boost"

        return {
            "tool": best_tool,
            "confidence": round(confidence, 3),
            "scores": {k: round(v, 3) for k, v in scores.items()},
            "reason": reason
        }