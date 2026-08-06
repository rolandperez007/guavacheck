"""
Austin Configuration

Central configuration loader for Austin.

Austin never hardcodes infrastructure values.
Everything should be driven by environment configuration.
"""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class AustinConfig:
    # Platform

    platform_name: str = os.getenv(
        "NEXT_PUBLIC_APP_NAME",
        "guavacheck",
    )

    environment: str = os.getenv(
        "APP_ENV",
        "development",
    )

    # AI

    model: str = os.getenv(
        "AUSTIN_MODEL",
        "gpt-5.5",
    )

    enabled: bool = os.getenv("AUSTIN_ENABLED", "true").lower() == "true"

    memory_enabled: bool = os.getenv("AUSTIN_MEMORY_ENABLED", "true").lower() == "true"

    # Database

    database_url: str = os.getenv(
        "DATABASE_URL",
        "",
    )

    supabase_url: str = os.getenv(
        "SUPABASE_URL",
        "",
    )

    # Logging

    log_level: str = os.getenv(
        "AUSTIN_LOG_LEVEL",
        "INFO",
    )

    # Monitoring

    health_interval: int = int(
        os.getenv(
            "AUSTIN_HEALTH_INTERVAL",
            "30",
        )
    )

    startup_timeout: int = int(
        os.getenv(
            "AUSTIN_STARTUP_TIMEOUT",
            "60",
        )
    )


config = AustinConfig()
