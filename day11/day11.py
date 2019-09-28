#!/usr/bin/env python3

from math import floor
from typing import Optional, Dict

# Ensure our square is within the 1X300 grid
LAST_CELL = 300


def part1(grid_serial_num: int) -> Dict[str, Optional[int]]:
    max_total = -1
    max_x = None
    max_y = None
    for x in range(1, LAST_CELL + 1):
        for y in range(1, LAST_CELL + 1):
            tp = _total_power(grid_serial_num, 3, x, y)
            if tp > max_total:
                max_total = tp
                max_x = x
                max_y = y
    return {"total": max_total, "x": max_x, "y": max_y}


def part2(grid_serial_num: int) -> int:
    return 0


def _total_power(grid_serial_num, grid_size, x, y: int) -> int:
    tp = 0
    for i in range(x, x + grid_size):
        if i > LAST_CELL:
            break
        for j in range(y, y + 3):
            if j > LAST_CELL:
                continue
            cpl = _cell_power_level(grid_serial_num, i, j)
            tp += cpl
            # print(f"i: {i}, j: {j}, cpl: {cpl}, tp: {tp}")
    return tp


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
