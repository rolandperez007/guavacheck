import jwt

SECRET_KEY = "change-this-in-env"

token = jwt.encode({"sub": "guava_user"}, SECRET_KEY, algorithm="HS256")

print(token)
