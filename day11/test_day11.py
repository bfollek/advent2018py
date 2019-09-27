from day11 import part1, part2, _cell_power_level

GRID_SERIAL_NUM = 5719


def test_part1():
    assert part1(GRID_SERIAL_NUM) == 0


def test_part2():
    assert part2(GRID_SERIAL_NUM) == 0


def test_cell_power_level():
    assert _cell_power_level(57, 122, 79) == -5
    assert _cell_power_level(39, 217, 196) == 0
    assert _cell_power_level(71, 101, 153) == 4
