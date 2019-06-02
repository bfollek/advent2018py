#!/usr/bin/env python3

from sys import maxsize

from coordinate import Coordinate
from plane import Plane


def part1(file_name):
    """
    Using only the Manhattan distance, determine the area around each coordinate by counting the number of integer X,Y locations that are closest to that coordinate (and aren't tied in distance to any other coordinate).

    What is the size of the largest area that isn't infinite?
    """
    with open(file_name) as f:
        lines = [line.rstrip() for line in f]
    p = Plane()
    for line in lines:
        x, y = map(int, line.split(","))
        p.add_coordinate(x, y)
    for x, y in p.empty_locations():
        _find_closest_coord(x, y, p.coordinates.values())
    # Find the finite coordinate closest to the most locations.
    # print(p.coordinates[(3, 4)].num_closest_to())
    # for c in p.coordinates.values():
    #     print(f"c: {(c.x, c.y)}, {c.num_closest_to()}, {p.is_infinite(c)}")
    return max(
        [c.num_closest_to() for c in p.coordinates.values() if not p.is_infinite(c)]
    )


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
