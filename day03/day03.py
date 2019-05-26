#!/usr/bin/env python3

from claim import Claim


def part1(file_name):
    """
    How many square inches of fabric are within two or more claims?
    """
    with open(file_name) as f:
        claims = [Claim.new_from_string(line.rstrip()) for line in f]
    d = {}
    # Count how many times each square inch appears in a claim
    for claim in claims:
        for sq_inch in claim.sq_inches():
            d.setdefault(sq_inch, 0)
            d[sq_inch] += 1
    # Count the # of values in d that are > 1
    return len([v for v in d.values() if v > 1])


def part2(file_name):
    """
    Find the one claim that doesn't overlap any other claim. Return its id.
    """
    with open(file_name) as f:
        claims = [Claim.new_from_string(line.rstrip()) for line in f]
    for claim in claims:
        if _no_overlap(claim, claims):
            return claim.id
    raise "Could not find claim that doesn't overlap any other claim."


def _no_overlap(claim, claims):
    for other in claims:
        if claim == other:
            continue
        if claim.overlaps(other):
            return False
    return True
