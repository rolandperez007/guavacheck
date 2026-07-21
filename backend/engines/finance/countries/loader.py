"""
GuavaCheck Finance Country Registry Loader

Loads country-level finance intelligence rules.

Responsibilities:
- load registry.json
- provide country lookup
- expose finance rules
"""

from pathlib import Path
import json
from typing import Dict, Any



class FinanceCountryRegistry:

    def __init__(self):

        self.registry_path = (
            Path(__file__).parent
            /
            "registry.json"
        )

        self.data = self._load()



    def _load(self) -> Dict[str, Any]:

        if not self.registry_path.exists():

            return {
                "countries": {}
            }


        with open(
            self.registry_path,
            "r",
            encoding="utf-8",
        ) as file:

            return json.load(file)



    def get_country(
        self,
        country_code: str,
    ) -> Dict[str, Any]:

        countries = self.data.get(
            "countries",
            {},
        )

        return countries.get(
            country_code.upper(),
            {},
        )



    def list_countries(self):

        return list(
            self.data.get(
                "countries",
                {},
            ).keys()
        )



    def get_finance_rules(
        self,
        country_code: str,
    ) -> Dict[str, Any]:

        country = self.get_country(
            country_code
        )

        return {

            "currency": country.get(
                "currency",
                {}
            ),

            "property_finance": country.get(
                "property_finance",
                {}
            ),

            "taxation": country.get(
                "taxation",
                {}
            ),

            "verification": country.get(
                "verification",
                {}

            ),

        }



finance_country_registry = FinanceCountryRegistry()