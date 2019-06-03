#!/usr/bin/env python3

from sys import maxsize

from coordinate import Coordinate
from grid import Grid


def part1(file_name):
    """
    Using only the Manhattan distance, determine the area around each coordinate by counting the number of integer X,Y locations that are closest to that coordinate (and aren't tied in distance to any other coordinate).

    What is the size of the largest area that isn't infinite?
    """
    with open(file_name) as f:
        lines = [line.rstrip() for line in f]
    g = Grid()
    for line in lines:
        x, y = map(int, line.split(","))
        g.add_coordinate(x, y)
    for x, y in g.empty_locations():
        _find_closest_coord(x, y, g.coordinates.values())
    # Find the finite coordinate closest to the most locations.
    return max([c.num_closest_to() for c in g.coordinates.values() if g.is_finite(c)])


def _find_closest_coord(x, y, coords):
    closest_dist = maxsize
    for c in coords:
        dist = c.distance(x, y)
        if dist < closest_dist:
            closest_dist = dist
            closest_coord = c
            tied = False
        elif dist == closest_dist:
            tied = True
    if not tied:
        closest_coord.closest_to.append((x, y))


def part2(file_name):
    """
    """
    pass
