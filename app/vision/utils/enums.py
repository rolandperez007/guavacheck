from enum import Enum


class ProjectStatus(str, Enum):
    DRAFT = "draft"
    GENERATING = "generating"
    READY = "ready"
    ARCHIVED = "archived"


class RoomType(str, Enum):
    LIVING_ROOM = "living_room"
    DINING_ROOM = "dining_room"
    KITCHEN = "kitchen"
    MASTER_BEDROOM = "master_bedroom"
    BEDROOM = "bedroom"
    BATHROOM = "bathroom"
    GUEST_ROOM = "guest_room"
    HOME_OFFICE = "home_office"
    CINEMA = "cinema"
    GYM = "gym"
    GARAGE = "garage"
    STAIRCASE = "staircase"
    BALCONY = "balcony"
    TERRACE = "terrace"
    GARDEN = "garden"


class DesignStyle(str, Enum):
    MODERN = "modern"
    MODERN_LUXURY = "modern_luxury"
    CONTEMPORARY = "contemporary"
    MINIMALIST = "minimalist"
    SCANDINAVIAN = "scandinavian"
    INDUSTRIAL = "industrial"
    MEDITERRANEAN = "mediterranean"
    TROPICAL = "tropical"
    CLASSIC = "classic"


class RenderStatus(str, Enum):
    PENDING = "pending"
    GENERATING = "generating"
    COMPLETED = "completed"
    FAILED = "failed"


class VisionProvider(str, Enum):
    OPENAI = "openai"
    GOOGLE = "google"
    STABILITY = "stability"
    LOCAL = "local"
