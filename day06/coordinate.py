from dataclasses import dataclass, field


@dataclass()
class Coordinate:
    _x: int
    _y: int
    _locations: list = field(default_factory=list)
    _infinite: bool = False

    def distance(self, x: int, y: int) -> int:
        """
        Manhattan distance
        """
        return abs(self._x - x) + abs(self._y - y)

    def area(self):
        """
        '...including the coordinate's location itself'
        """
        return len(self._locations) + 1

    def add_location(self, x, y, infinite):
        self._locations.append((x, y))
        # If infinite is True, set self._infinite to True.
        # If infinite is False, leave self._infinite unchanged.
        # We don't want to clear it after an earlier call set it.
        if infinite:
            self._infinite = True

    def is_infinite(self):
        return self._infinite
