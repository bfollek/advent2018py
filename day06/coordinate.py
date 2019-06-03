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

    def add_finite_location(self, x, y):
        # Leave the _infinite flag alone. Once it's True, we don't want to clear it.
        self._locations.append((x, y))

    def add_infinite_location(self, x, y):
        self._locations.append((x, y))
        self._infinite = True

    def is_infinite(self):
        return self._infinite
