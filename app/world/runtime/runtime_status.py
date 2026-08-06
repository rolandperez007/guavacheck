from dataclasses import dataclass



@dataclass
class RuntimeStatus:

    status: str = "offline"

    templates: int = 0

    countries: int = 0

    districts: int = 0

    engines: int = 0