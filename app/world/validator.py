from pathlib import Path


REQUIRED = [

    "01-identity.md",

    "02-government.md",

    "03-geography.md",

    "04-demographics.md",

    "05-economy.md",

    "06-currency.md",

    "07-banking.md",

    "08-taxation.md",

    "09-mortgages.md",

    "10-property.md",

    "11-construction.md",

    "12-legal.md",

    "13-localization.md",

    "14-utilities.md",

    "15-transport.md",

    "16-security.md",

    "17-austin.md",

]


def validate_country(path: Path):

    missing = []

    for file in REQUIRED:

        if not (path / file).exists():

            missing.append(file)

    return missing