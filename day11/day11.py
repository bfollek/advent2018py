#!/usr/bin/env python3

from collections import namedtuple
from math import floor
import numpy as np
from typing import Any, Dict, NamedTuple, Optional, Sequence

# The grid is 1X300
LAST_CELL = 300

Result = NamedTuple(
    "Result",
    [
        ("total", Optional[int]),
        ("x", Optional[int]),
        ("y", Optional[int]),
        ("grid_size", Optional[int]),
    ],
)


def part1(grid_serial_num: int) -> Result:
    return _find_best_grid(grid_serial_num, [3])


def part2(grid_serial_num: int) -> Result:
    # Test squares from 1X1 to 300X300
    grid_sizes = range(1, LAST_CELL + 1)
    return _find_best_grid(grid_serial_num, grid_sizes)


def _find_best_grid(grid_serial_num: int, grid_sizes: Sequence[int]) -> Result:
    ary = _create_array(grid_serial_num)
    max_total = None
    best_grid_size = None
    max_x = None
    max_y = None
    for x in range(ary[0].size):
        for y in range(ary[0].size):
            for grid_size in grid_sizes:
                tp = _total_power(ary, grid_size, x, y)
                if max_total is None:
                    max_total = tp
                elif tp and tp > max_total:
                    max_total = tp
                    max_x = x
                    max_y = y
                    best_grid_size = grid_size
    return Result(max_total, max_x, max_y, best_grid_size)


def _total_power(ary: np.ndarray, grid_size, x, y: int) -> Optional[int]:
    # Bounds-check. A slice handles rogue indices automatically, but we
    # don't want to inadvertently return unreliable results in those cases.
    if grid_size + x >= ary[0].size:
        return None
    if grid_size + y >= ary[0].size:
        return None
    grid = ary[x : x + grid_size, y : y + grid_size]
    return grid.sum()


def _create_array(grid_serial_num: int) -> np.ndarray:
    cell_power_levels = []
    for i in range(LAST_CELL):
        for j in range(LAST_CELL):
            cell_power_levels.append(_cell_power_level(grid_serial_num, i, j))
    return np.array(cell_power_levels, dtype=int).reshape(LAST_CELL, LAST_CELL)


def _cell_power_level(grid_serial_num, x, y: int) -> int:
    """
    Calculate the power level of a fuel cell.
    """
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
