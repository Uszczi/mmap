from enum import Enum


class StrEnum(str, Enum):
    def __repr__(self) -> str:
        return f"'{self.value}'"


class ActivityType(StrEnum):
    BIKE = "BIKE"
    WALK = "WALK"
    ROLLERBLADE = "ROLLERBLADE"
    RUN = "RUN"
