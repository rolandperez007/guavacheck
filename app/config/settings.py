from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str = "GuavaCheck"

    ENVIRONMENT: str = "development"

    # Database
    DATABASE_URL: str = ""

    # Security
    SECRET_KEY: str = ""

    # Redis
    REDIS_URL: str = ""

    # AI Providers
    OPENAI_API_KEY: str = ""

    # Payments
    STRIPE_SECRET_KEY: str = ""
    PAYSTACK_SECRET_KEY: str = ""

    # Supabase
    SUPABASE_URL: str = ""
    SUPABASE_SERVICE_ROLE_KEY: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore",
    )


@lru_cache
def get_settings():

    return Settings()