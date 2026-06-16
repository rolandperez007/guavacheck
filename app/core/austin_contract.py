from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class AustinResponse:
    user_id: str
    query: str
    parsed: Dict[str, Any]
    analysis: Dict[str, Any]
    response: str

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "query": self.query,
            "parsed": self.parsed,
            "analysis": self.analysis,
            "response": str(self.response),
        }