from circle import Circle

PLACE_TESTS = {
    1: [0, 1],
    2: [0, 2, 1],
    3: [0, 2, 1, 3],
    4: [0, 4, 2, 1, 3],
    5: [0, 4, 2, 5, 1, 3],
    22: [
        0,
        16,
        8,
        17,
        4,
        18,
        9,
        19,
        2,
        20,
        10,
        21,
        5,
        22,
        11,
        1,
        12,
        6,
        13,
        3,
        14,
        7,
        15,
    ],
}


def test_init():
    c = Circle()
    assert c._data.to_list() == [0]
    assert c.current.data == 0


def test_place():
    for input, lst in PLACE_TESTS.items():
        c = Circle()
        for i in range(1, input + 1):
            c.place(i)
        assert c.current.data == input
        assert c._data.to_list() == lst


def test_del():
    c = Circle()
    for i in range(1, 4):
        c.place(i)
    lst = PLACE_TESTS[3]
    assert c.current.data == 3
    assert c._data.to_list() == lst
    c.remove(c.current)
    assert c.current.data == 0
    assert c._data.to_list() == [0, 2, 1]
