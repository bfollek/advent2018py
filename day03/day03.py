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
    Find the one claim that doesn't overlap any other claim.
    """
    pass


# part2
# for each sq inch
#    which claims claim it?
# remove all values that contain more than one claim
# value that's left is the answer
