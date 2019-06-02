from dataclasses import dataclass, field
from sys import maxsize

from coordinate import Coordinate


@dataclass()
class Grid:
    _min_x: int = maxsize
    _max_x: int = -1
    _min_y: int = maxsize
    _max_y: int = -1
    coordinates: dict = field(default_factory=dict)

    def add_coordinate(self, x, y):
        "Expand the bounds of the grid to include this coordinate."
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

    def is_finite(self, c: Coordinate) -> bool:
        "Is the coordinate finite on this grid?"
        return self._min_x < c.x < self._max_x and self._min_y < c.y < self._max_y

    def empty_locations(self):
        return (
            (x, y)
            for x in range(self._min_x + 1, self._max_x)
            for y in range(self._min_y + 1, self._max_y)
            if not (x, y) in self.coordinates
        )
