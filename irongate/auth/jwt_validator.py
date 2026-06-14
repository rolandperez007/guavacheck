import jwt

SECRET_KEY = "change-this-in-env"

ALGORITHM = "HS256"


def validate_jwt(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        return {"valid": True, "payload": payload}

    except jwt.ExpiredSignatureError:
        return {"valid": False, "reason": "Token expired"}

    except jwt.InvalidTokenError:
        return {"valid": False, "reason": "Invalid token"}
