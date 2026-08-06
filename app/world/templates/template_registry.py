"""
Stores reusable world templates.
"""


class TemplateRegistry:


    def __init__(self):

        self.templates = {}



    def register(
        self,
        name,
        template,
    ):

        self.templates[name] = template



    def get(
        self,
        name,
    ):

        return self.templates.get(name)