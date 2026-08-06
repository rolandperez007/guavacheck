from pathlib import Path


WORLD_ROOT = Path("docs/world")


def load_country(country: str):

    path = WORLD_ROOT / "countries"

    results = []

    for continent in path.iterdir():

        candidate = continent / country.lower()

        if candidate.exists():

            for doc in sorted(candidate.glob("*.md")):

                results.append(doc)

    return results