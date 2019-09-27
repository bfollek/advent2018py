from day11 import part1, part2, _cell_power_level, _total_power

GRID_SERIAL_NUM = 5719


def test_part1():
    d = part1(GRID_SERIAL_NUM)
    assert d["total"] == 29
    assert d["x"] == 21
    assert d["y"] == 34


def test_part2():
    # assert part2(GRID_SERIAL_NUM) == 0
    pass


def test_total_power():
    assert _total_power(18, 33, 45) == 29
    assert _total_power(42, 21, 61) == 30


def test_cell_power_level():
    assert _cell_power_level(57, 122, 79) == -5
    assert _cell_power_level(39, 217, 196) == 0
    assert _cell_power_level(71, 101, 153) == 4
