from dataclasses import dataclass


@dataclass
class KernelState:

    status: str = "offline"

    countries_loaded: int = 0

    districts_loaded: int = 0

    engines_connected: int = 0