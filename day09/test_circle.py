from circle import Circle

PLACE_TESTS = {
    #  (_current, _list)
    1: (1, [0, 1]),
    2: (1, [0, 2, 1]),
    3: (3, [0, 2, 1, 3]),
    4: (1, [0, 4, 2, 1, 3]),
    5: (3, [0, 4, 2, 5, 1, 3]),
    22: (
        13,
        [
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
    ),
}


def test_init():
    c = Circle()
    assert c._list == [0]
    assert c._current == 0


def test_place():
    for input, (current, list) in PLACE_TESTS.items():
        c = Circle()
        for i in range(1, input + 1):
            c.place(i)
        assert c._current == current
        assert c._list == list
