"""
World Template Engine

Controls inheritance between:

World
 |
Country
 |
District
"""


class TemplateEngine:


    def merge(
        self,
        base,
        override,
    ):

        result = {}

        result.update(base)

        result.update(
            override
        )

        return result