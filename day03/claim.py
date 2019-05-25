from dataclasses import dataclass
from typing import Tuple


@dataclass
class Claim:
    id: str
    x: int
    y: int
    width: int
    height: int

    def sq_inches(self: "Claim") -> Tuple[int, int]:
        """
        Return a list of (int, int) tuples. Each tuple is a square inch in the claim.
        """
        return [
            (i, j)
            for i in range(self.x, self.x + self.width)
            for j in range(self.y, self.y + self.height)
        ]

    def overlaps(self: "Claim", other: "Claim") -> bool:
        self_set = set(self.sq_inches())
        other_set = set(other.sq_inches())
        return len(self_set & other_set) > 0
