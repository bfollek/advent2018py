#!/usr/bin/env python3

from dataclasses import dataclass
import re


@dataclass
class Claim:
    id: str
    x: int
    y: int
    width: int
    height: int


# #14 @ 690,863: 12x20
CLAIM_REGEX = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")


def part1(file_name):
    """
    How many square inches of fabric are within two or more claims?
    """
    with open(file_name) as f:
        claims = [_line_to_claim(line.rstrip()) for line in f]
    d = {}
    # Count how many times each square inch appears in a claim
    for claim in claims:
        for i in range(claim.x, claim.x + claim.width):
            for j in range(claim.y, claim.y + claim.height):
                sq_inch = (i, j)
                d.setdefault(sq_inch, 0)
                d[sq_inch] += 1
    # Count the # of values in d that are > 1
    return len([v for v in d.values() if v > 1])


def _line_to_claim(line):
    m = re.search(CLAIM_REGEX, line)
    flds = list(m.groups())
    # Convert to int where necessary
    for i in range(1, len(flds)):
        flds[i] = int(flds[i])
    return Claim(*flds)
