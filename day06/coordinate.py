from dataclasses import dataclass, field


@dataclass()
class Coordinate:
    x: int
    y: int
    closest_to: list = field(default_factory=list)

    def distance(self, x: int, y: int) -> int:
        """
        Manhattan distance
        """
        return abs(self.x - x) + abs(self.y - y)

    def num_closest_to(self):
        """
        '...including the coordinate's location itself'
        """
        return len(self.closest_to) + 1
