from dataclasses import dataclass, field


@dataclass()
class Coordinate:
    point: tuple  # (x, y)
    infinite: bool = False

    def __post_init__(self):
        # Key is location point tuple (x, y). Value is distance from self to point.
        self.locations = {}

    def distance(self, point: tuple) -> int:
        """
        Manhattan distance
        """
        return abs(self.point[0] - point[0]) + abs(self.point[1] - point[1])

    @property
    def area(self):
        """
        '...including the coordinate's location itself'
        """
        return len(self.locations) + 1

    def add_location(self, point, infinite_location):
        self.locations[point] = self.distance(point)
        # If infinite is True, set self._infinite to True.
        # If infinite is False, leave self._infinite unchanged.
        # We don't want to clear it after an earlier call set it.
        if infinite_location:
            self.infinite = True
