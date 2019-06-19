from day08 import part1, part2


def test_part1():
    assert part1("day08/day08_short.dat") == 138
    assert part1("day08/day08.dat") == 43996


def test_part2():
    assert part2("day08/day08_short.dat") == 66
    assert part2("day08/day08.dat") == 35189
