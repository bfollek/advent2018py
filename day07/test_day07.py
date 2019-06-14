from day07 import part1, part2


def test_part1():
    assert part1("day07/day07.dat") == "HEGMPOAWBFCDITVXYZRKUQNSLJ"
    pass


def test_part2():
    assert part2("day07/day07.dat", num_workers=5) == 1226
