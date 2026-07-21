"""
Registry Loader

Loads and manages global government intelligence
configuration files for guavacheck.

Sources:

- registry.json
- providers.json
- connectors.json
- confidence_rules.json
- compliance_matrix.json
"""

from pathlib import Path
import json
from typing import Any, Dict


class RegistryLoader:

    def __init__(self, base_path: str | None = None):

        if base_path:

            self.base_path = Path(base_path)

        else:

            self.base_path = (
                Path(__file__)
                .resolve()
                .parents[3]
                / "world"
                / "government"
            )


        self.files = {

            "registry":
                "registry.json",

            "providers":
                "providers.json",

            "connectors":
                "connectors.json",

            "confidence_rules":
                "confidence_rules.json",

            "compliance":
                "compliance_matrix.json",

        }


        self.cache: Dict[str, Any] = {}


    def load_file(
        self,
        file_name: str,
    ) -> Dict[str, Any]:

        path = self.base_path / file_name


        if not path.exists():

            raise FileNotFoundError(
                f"Government intelligence file missing: {path}"
            )


        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)



    def load_all(self) -> Dict[str, Any]:

        data = {}


        for key, file_name in self.files.items():

            data[key] = self.load_file(
                file_name
            )


        self.cache = data


        return data



    def get(
        self,
        key: str,
    ) -> Any:

        if not self.cache:

            self.load_all()


        return self.cache.get(key)



    def reload(self) -> Dict[str, Any]:

        self.cache = {}

        return self.load_all()



    def available_modules(self) -> list[str]:

        return list(
            self.files.keys()
        )