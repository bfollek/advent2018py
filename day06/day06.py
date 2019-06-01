#!/usr/bin/env python3

from sys import maxsize

from coordinate import Coordinate
from plane import Plane


def part1(file_name):
    """
    What is the size of the largest area that isn't infinite?
    """
    with open(file_name) as f:
        lines = [line.rstrip() for line in f]
    pl = Plane()
    coords = []
    for line in lines:
        x, y = map(int, line.split(","))
        c = Coordinate(x, y)
        coords.append(c)
        pl.expand(c)
    print(f"left: {pl.left}, right: {pl.right}, bottom: {pl.bottom}, top: {pl.top}")
    print(f"before filter: {len(coords)}")
    # Filter out infinite edge coordinates
    coords = [c for c in coords if pl.surrounds(c)]
    print(f"after filter: {len(coords)}")
    return None
    # Brute force:
    # plane.locations generator
    # iterate it
    # Figure out which coordinate is closest, add location to closest_to[]
    #   Remember that ties don't count
    # if md > max_md
    #   max_md = md
    #   max_coord = coord
    #   tied == False
    # elif md == max_md
    #   tied == True
    # # else it's less, nothing to do


def part2(file_name):
    """
    """
    pass
