#!/usr/bin/env python3

from math import floor
from typing import Any, Optional, Dict
import numpy as np

# The grid is 1X300
LAST_CELL = 300


def part1(grid_serial_num: int) -> Dict[str, Optional[int]]:
    ary = _create_array(grid_serial_num)
    max_total = None
    max_x = None
    max_y = None
    for x in range(ary[0].size):
        for y in range(ary[0].size):
            tp = _total_power(ary, 3, x, y)
            if max_total is None:
                max_total = tp
            elif tp and tp > max_total:
                max_total = tp
                max_x = x
                max_y = y
    return {"total": max_total, "x": max_x, "y": max_y}


def part2(grid_serial_num: int) -> Dict[str, Optional[int]]:
    ary = _create_array(grid_serial_num)
    max_total = None
    best_grid_size = None
    max_x = None
    max_y = None
    for x in range(ary[0].size):
        for y in range(ary[0].size):
            # Test squares from 1X1 to 300X300
            for grid_size in range(1, LAST_CELL + 1):
                tp = _total_power(ary, grid_size, x, y)
                if max_total is None:
                    max_total = tp
                elif tp and tp > max_total:
                    max_total = tp
                    max_x = x
                    max_y = y
                    best_grid_size = grid_size
    return {"total": max_total, "x": max_x, "y": max_y, "grid size": best_grid_size}


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
