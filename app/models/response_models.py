# app/models/response_models.py

from pydantic import BaseModel


class AustinResponse(BaseModel):
    input: str
    intent: str
    mode: str
    agent: str
    data: dict
