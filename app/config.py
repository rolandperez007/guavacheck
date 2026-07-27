import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "")
    STRIPE_PUBLISHABLE_KEY = os.getenv("STRIPE_PUBLISHABLE_KEY", "")
    STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET", "")

    FRONTEND_URL = os.getenv(
        "FRONTEND_URL",
        "http://localhost:3000",
    )


settings = Settings()