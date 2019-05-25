from dataclasses import dataclass
import re
from typing import Tuple


@dataclass
class Claim:
    _id: str
    _x: int
    _y: int
    _width: int
    _height: int

    # #14 @ 690,863: 12x20
    _CLAIM_REGEX = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")

    def sq_inches(self: "Claim") -> Tuple[int, int]:
        """
        Return a list of (int, int) tuples. Each tuple is a square inch in the claim.
        """
        return [
            (i, j)
            for i in range(self._x, self._x + self._width)
            for j in range(self._y, self._y + self._height)
        ]

    def overlaps(self: "Claim", other: "Claim") -> bool:
        self_set = set(self.sq_inches())
        other_set = set(other.sq_inches())
        return len(self_set & other_set) > 0

    @classmethod
    def new_from_string(cls, s: str) -> "Claim":
        m = re.search(cls._CLAIM_REGEX, s)
        flds = list(m.groups())
        # Convert to int where necessary
        for i in range(1, len(flds)):
            flds[i] = int(flds[i])
        return Claim(*flds)
