class ThreeEngine:
    def __init__(self):
        self.scene = {
            "objects": [],
            "camera": {"position": [0, 0, 5], "rotation": [0, 0, 0]},
            "lights": [],
        }

    def add_object(self, obj_type: str, position: list, metadata: dict = None):
        obj = {"type": obj_type, "position": position, "metadata": metadata or {}}

        self.scene["objects"].append(obj)
        return obj

    def update_object(self, index: int, updates: dict):
        if 0 <= index < len(self.scene["objects"]):
            self.scene["objects"][index].update(updates)

        return self.scene

    def get_scene(self):
        return self.scene
