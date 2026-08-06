"""
World YAML Loader

Loads world intelligence files
from the docs/world directory.
"""


from pathlib import Path

import yaml



class YAMLWorldLoader:


    def load_file(
        self,
        path,
    ):

        file_path = Path(path)


        with open(
            file_path,
            "r",
            encoding="utf-8",
        ) as file:

            return yaml.safe_load(
                file
            )