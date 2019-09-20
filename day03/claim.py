from dataclasses import dataclass
from functools import lru_cache
import re
from typing import List, Tuple, Type


# eq and frozen make Claim hashable, so that we can cache _sq_inches().
@dataclass(eq=True, frozen=True)
class Claim:
    id: str
    _x: int
    _y: int
    _width: int
    _height: int

    # #14 @ 690,863: 12x20
    CLAIM_REGEX = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")

    def overlaps(self: "Claim", other: "Claim") -> bool:
        self_set = set(self.sq_inches)
        other_set = set(other.sq_inches)
        return len(self_set & other_set) > 0

    @property
    def sq_inches(self: "Claim") -> List[Tuple[int, int]]:
        return self._sq_inches()

    # Large cache makes things faster. Jump to 4096 didn't help.
    @lru_cache(maxsize=2048)
    def _sq_inches(self: "Claim") -> List[Tuple[int, int]]:
        """
        Returns a list of the square inches in the claim.
        """
        return [
            (i, j)
            for i in range(self._x, self._x + self._width)
            for j in range(self._y, self._y + self._height)
        ]

    @classmethod
    def new_from_string(cls: Type["Claim"], s: str) -> "Claim":
        m = re.search(cls.CLAIM_REGEX, s)
        if not m:
            raise Exception(f"Can't create Claim: can't parse string [{s}]")
        tokens = list(m.groups())
        # Convert to int where necessary
        flds = []
        for i in range(1, len(tokens)):
            flds.append(int(tokens[i]))
        return Claim(tokens[0], *flds)
