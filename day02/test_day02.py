from day02 import part1, part2, _check_chars, _diff_by_1


def test_part1():
    assert part1("day02/day02.dat") == 8715


def test_part2():
    assert part2("day02/day02.dat") == "fvstwblgqkhpuixdrnevmaycd"


def test_check_chars():
    assert _check_chars("AAAABBBCCDAABBB") == (True, False)
    assert _check_chars("AAAABBCCDAAB") == (True, True)
    assert _check_chars("AACCAABBCDAAB") == (False, True)
    assert _check_chars("AACAABBCCDABACB") == (False, False)


def test_diff_by_1():
    assert _diff_by_1("ABCD", "ABCX") == (True, "ABC")
    assert _diff_by_1("AZBCD", "APBCX") == (False, None)
    assert _diff_by_1("ABCD", "ABCD") == (False, None)  # Same string
    assert _diff_by_1("ABCDE", "ABCD") == (False, None)  # Different lengths
