from pydantic import BaseModel
from typing import Optional, Dict, Any


class AustinExecuteRequest(BaseModel):
    input: str
    context: Optional[Dict[str, Any]] = {}
