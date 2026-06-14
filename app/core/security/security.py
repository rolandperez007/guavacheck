from jose import JWTError, jwt
from fastapi import HTTPException, Header, status
from pydantic import BaseModel
from typing import Optional
from fastapi import APIRouter, Depends
from app.core.security.security import get_current_user

# ⚠️ Move this to .env later
SECRET_KEY = "CHANGE_ME_SUPER_SECRET"
ALGORITHM = "HS256"


class User(BaseModel):
    id: str
    org_id: Optional[str] = None
    role: Optional[str] = "user"


# -----------------------------
# TOKEN DECODER
# -----------------------------
def decode_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        )


# -----------------------------
# CURRENT USER
# -----------------------------
def get_current_user(authorization: str = Header(None)) -> User:
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing authorization header",
        )

    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise Exception()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid auth format"
        )

    payload = decode_token(token)

    return User(
        id=payload.get("sub"),
        org_id=payload.get("org_id"),
        role=payload.get("role", "user"),
    )
