from datetime import datetime, timedelta, timezone

from jose import jwt

from app.config.settings import get_settings


settings = get_settings()


ALGORITHM = "HS256"


def create_access_token(
    user_id: str
):

    expire = (
        datetime.now(timezone.utc)
        +
        timedelta(hours=24)
    )


    payload = {

        "sub": user_id,

        "exp": expire
    }


    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=ALGORITHM
    )