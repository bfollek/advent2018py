from dataclasses import dataclass
from sys import maxsize

from coordinate import Coordinate


@dataclass()
class Plane:
    left: int = maxsize
    right: int = -1
    bottom: int = maxsize
    top: int = -1

    def expand(self, c: Coordinate):
        "Expand the bounds of the plain to include this coordinate."
        if c.x < self.left:
            self.left = c.x
        # No elif because the first coordinate will move both left and right.
        if c.x > self.right:
            self.right = c.x
        if c.y < self.bottom:
            self.bottom = c.y
        if c.y > self.top:
            self.top = c.y

    def surrounds(self, c: Coordinate) -> bool:
        "Does this plain surround the coordinate? True if the coordinate doesn't tourch or cross a border."
        return self.left < c.x < self.right and self.bottom < c.y < self.top
