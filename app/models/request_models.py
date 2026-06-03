from pydantic import BaseModel

class AustinExecuteRequest(BaseModel):

    input: str

    session_id: str

    user_id: str

    context: dict = {}