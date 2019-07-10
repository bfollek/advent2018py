from circle import Circle


def test_init():
    c = Circle()
    assert c._list == [0]
    assert c._current == 0


def test_place_1():
    c = Circle()
    c.place(1)
    assert c._list == [0, 1]
    assert c._current == 1


def test_place_2():
    c = Circle()
    c.place(1)
    c.place(2)
    assert c._list == [0, 2, 1]
    assert c._current == 1


def test_place_3():
    c = Circle()
    c.place(1)
    c.place(2)
    c.place(3)
    assert c._list == [0, 2, 1, 3]
    assert c._current == 3


def test_place_4():
    c = Circle()
    c.place(1)
    c.place(2)
    c.place(3)
    c.place(4)
    assert c._list == [0, 4, 2, 1, 3]
    assert c._current == 1


def test_place_5():
    c = Circle()
    c.place(1)
    c.place(2)
    c.place(3)
    c.place(4)
    c.place(5)
    assert c._list == [0, 4, 2, 5, 1, 3]
    assert c._current == 3
