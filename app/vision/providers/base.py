from abc import ABC
from abc import abstractmethod


class VisionProvider(ABC):

    @abstractmethod
    def generate_interior(
        self,
        prompt: str,
    ):
        pass

    @abstractmethod
    def generate_exterior(
        self,
        prompt: str,
    ):
        pass

    @abstractmethod
    def generate_floorplan(
        self,
        prompt: str,
    ):
        pass