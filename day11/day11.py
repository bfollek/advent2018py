#!/usr/bin/env python3

from math import floor


def part1(file_name):
    pass


def part2(file_name):
    pass


def _cell_power_level(grid_serial_num, x, y: int) -> int:
    """
    Calculate the power level of a fuel cell.
    """
    # For example, to find the power level of the fuel cell at 3,5 in a grid with serial number 8:

    #     The rack ID is 3 + 10 = 13.
    #     The power level starts at 13 * 5 = 65.
    #     Adding the serial number produces 65 + 8 = 73.
    #     Multiplying by the rack ID produces 73 * 13 = 949.
    #     The hundreds digit of 949 is 9.
    #     Subtracting 5 produces 9 - 5 = 4.

    # So, the power level of this fuel cell is 4.

    # Here are some more example power levels:

    #     Fuel cell at  122,79, grid serial number 57: power level -5.
    #     Fuel cell at 217,196, grid serial number 39: power level  0.
    #     Fuel cell at 101,153, grid serial number 71: power level  4.
    # Find the fuel cell's rack ID, which is its X coordinate plus 10.

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
