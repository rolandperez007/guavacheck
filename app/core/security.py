from fastapi import HTTPException, Security
from fastapi.security import APIKeyHeader

API_SECRET = "dev-secret-change-this"

api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)


def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key == API_SECRET:
        return api_key

    raise HTTPException(status_code=401, detail="Unauthorized")
