import day11

GRID_SERIAL_NUM = 5719


def test_part1():
    d = day11.part1(GRID_SERIAL_NUM)
    assert d.total == 29
    assert d.x == 21
    assert d.y == 34


def test_part2():
    d = day11.part2(GRID_SERIAL_NUM)
    assert d.total == 124
    assert d.x == 90
    assert d.y == 244
    assert d.grid_size == 16


def test_total_power():
    assert day11._total_power(day11._create_array(18), 3, 33, 45) == 29
    assert day11._total_power(day11._create_array(42), 3, 21, 61) == 30


def test_cell_power_level():
    assert day11._cell_power_level(57, 122, 79) == -5
    assert day11._cell_power_level(39, 217, 196) == 0
    assert day11._cell_power_level(71, 101, 153) == 4
