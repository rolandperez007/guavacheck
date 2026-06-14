from dataclasses import dataclass


@dataclass
class PolicyContext:
    environment: str = "dev"
    user_tier: str = "free"
    system_mode: str = "balanced"
