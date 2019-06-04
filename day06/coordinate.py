from dataclasses import dataclass, field


@dataclass()
class Coordinate:
    _point: tuple  # (x, y)
    _locations: dict = field(default_factory=dict)
    _infinite: bool = False

    def distance(self, point: tuple) -> int:
        """
        Manhattan distance
        """
        return abs(self._point[0] - point[0]) + abs(self._point[1] - point[1])

    def area(self):
        """
        '...including the coordinate's location itself'
        """
        return len(self._locations) + 1

    def add_location(self, point, infinite):
        self._locations[point] = self.distance(point)
        # If infinite is True, set self._infinite to True.
        # If infinite is False, leave self._infinite unchanged.
        # We don't want to clear it after an earlier call set it.
        if infinite:
            self._infinite = True

    def is_infinite(self):
        return self._infinite
