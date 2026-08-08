from fastapi import Depends, HTTPException

from fastapi.security import OAuth2PasswordBearer

from jose import jwt, JWTError

from app.config.settings import get_settings


settings = get_settings()


oauth_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


def get_current_user(
    token: str = Depends(oauth_scheme)
):

    try:

        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=["HS256"]
        )


        user_id = payload.get("sub")


        if not user_id:

            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )


        return user_id


    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )