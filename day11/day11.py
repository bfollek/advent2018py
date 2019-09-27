#!/usr/bin/env python3

from math import floor


def part1(grid_serial_num):
    return 0


def part2(grid_serial_num):
    return 0


def _cell_power_level(grid_serial_num, x, y: int) -> int:
    """
    Calculate the power level of a fuel cell.
    """
    rack_id = x + 10
    # Begin with a power level of the rack ID times the Y coordinate.
    power_level = rack_id * y
    # Increase the power level by the value of the grid serial number (your puzzle input).
    power_level += grid_serial_num
    # Set the power level to itself multiplied by the rack ID.
    power_level *= rack_id
    # Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).
    power_level = floor(power_level % 1000 / 100)
    # Subtract 5 from the power level.
    return power_level - 5
