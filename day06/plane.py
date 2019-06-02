from dataclasses import dataclass, field
from sys import maxsize

from coordinate import Coordinate


@dataclass()
class Plane:
    _min_x: int = maxsize
    _max_x: int = -1
    _min_y: int = maxsize
    _max_y: int = -1
    coordinates: dict = field(default_factory=dict)

    def add_coordinate(self, x, y):
        "Expand the bounds of the plain to include this coordinate."
        if x < self._min_x:
            self._min_x = x
        # No elif because first coordinate will change both min and max.
        if x > self._max_x:
            self._max_x = x
        if y < self._min_y:
            self._min_y = y
        if y > self._max_y:
            self._max_y = y
        c = Coordinate(x, y)
        self.coordinates[(x, y)] = c
        return c

    def is_infinite(self, c: Coordinate) -> bool:
        "Is the coordinate infinite on this plane?"
        return (
            c.x <= self._min_x
            or c.x >= self._max_x
            or c.y <= self._min_y
            or c.y >= self._max_y
        )

    def is_finite(self, c: Coordinate) -> bool:
        "Is the coordinate finite on this plane?"
        return not self.is_infinite(c)

    def empty_locations(self):
        # Make a square
        # limit = (self._max_x if self._max_x > self._max_y else self._max_y) + 1
        return (
            (x, y)
            for x in range(self._min_x + 1, self._max_x)
            for y in range(self._min_y + 1, self._max_y)
            if not (x, y) in self.coordinates
        )
