#!/usr/bin/env python3

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
        g.add_coordinate((x, y))
    g.scan()
    c = g.largest_finite_area()
    return c.area()


def part2(file_name):
    """
    What is the size of the region containing all locations which have a total distance to all given coordinates of less than 10000?
    """
    pass
