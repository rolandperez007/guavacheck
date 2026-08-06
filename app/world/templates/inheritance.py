"""
Inheritance Resolver
"""


class InheritanceResolver:


    def inherit(
        self,
        parent,
        child,
    ):

        merged = {}

        merged.update(parent)

        merged.update(child)

        return merged