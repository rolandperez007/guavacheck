"""
Geography Resolver

Resolves location hierarchy.
"""


class GeographyResolver:


    def __init__(
        self,
        registry,
    ):

        self.registry = registry



    def resolve_path(
        self,
        location,
    ):

        node = self.registry.get(
            location
        )


        path = []


        while node:

            path.append(
                node.name
            )


            if node.parent:

                node = self.registry.get(
                    node.parent
                )

            else:

                node = None


        return list(
            reversed(path)
        )