from app.vision.providers.base import VisionProvider


class StabilityProvider(VisionProvider):
    def generate_interior(self, prompt: str):
        raise NotImplementedError

    def generate_exterior(self, prompt: str):
        raise NotImplementedError

    def generate_floorplan(self, prompt: str):
        raise NotImplementedError
