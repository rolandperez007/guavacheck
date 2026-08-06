"""
Country Intelligence Instance

Represents a fully composed country.
"""


from dataclasses import dataclass



@dataclass
class CountryInstance:


    name: str

    data: dict