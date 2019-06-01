from dataclasses import dataclass, field


@dataclass()
class Coordinate:
    x: int
    y: int
    closest_to: list = field(default_factory=list)

    def distance(self, other: "Coordinate") -> int:
        # Manhattan distance
        return abs(self.x - other.x) + abs(self.y - other.y)
