from dataclasses import dataclass, field
from sys import maxsize

from coordinate import Coordinate


@dataclass()
class Grid:
    _coord_dict: dict = field(default_factory=dict)

    SIZE = 400

    def add_coordinate(self, point):
        self._check_size(point)
        c = Coordinate(point)
        self._coord_dict[point] = c
        return c

    def scan(self):
        for point in self._empty_locations():
            self._find_closest_coordinate(point)

    def largest_finite_area(self):
        """
        Find the coordinate with the largest finite area.
        """
        largest_area = -1
        largest_coord = None
        for c in self._coord_dict.values():
            if c.is_infinite():
                continue
            if c.area() > largest_area:
                largest_area = c.area()
                largest_coord = c
        return largest_coord

    def _check_size(self, point):
        if point[0] >= self.SIZE or point[1] >= self.SIZE:
            raise ValueError(
                f"Grid size error! Size is {self.SIZE}, input is ({point})"
            )

    def _empty_locations(self):
        return (
            (x, y)
            for x in range(0, self.SIZE)
            for y in range(0, self.SIZE)
            if not (x, y) in self._coord_dict
        )

    def _find_closest_coordinate(self, point):
        closest_dist = maxsize
        for c in self._coord_dict.values():
            dist = c.distance(point)
            if dist < closest_dist:
                closest_dist = dist
                closest_coord = c
                tied = False
            elif dist == closest_dist:
                tied = True
        if not tied:
            infinite = self._touches_edge(point[0]) or self._touches_edge(point[1])
            closest_coord.add_location(point, infinite)

    def _touches_edge(self, i):
        return i == 0 or i == self.SIZE - 1
