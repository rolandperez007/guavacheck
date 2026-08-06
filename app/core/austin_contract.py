from dataclasses import dataclass
from typing import Any


@dataclass
class AustinResponse:
    user_id: str
    query: str
    parsed: dict[str, Any]
    analysis: dict[str, Any]
    response: str

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "query": self.query,
            "parsed": self.parsed,
            "analysis": self.analysis,
            "response": str(self.response),
        }
