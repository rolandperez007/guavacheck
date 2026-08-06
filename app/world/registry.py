from __future__ import annotations

import json

from pathlib import Path


REGISTRY_ROOT = Path("docs/world/registry")


def load_registry(name: str):

    file = REGISTRY_ROOT / f"{name}.json"

    if not file.exists():

        return {}

    with open(file, encoding="utf-8") as fp:

        return json.load(fp)


countries = load_registry("countries")

continents = load_registry("continents")

regions = load_registry("regions")

currencies = load_registry("currencies")

languages = load_registry("languages")

timezones = load_registry("timezones")

capabilities = load_registry("capabilities")