from coordinate import Coordinate


def test_distance():
    c = Coordinate(1, 1)
    assert c.distance(15, 20) == 33
    c = Coordinate(15, 20)
    assert c.distance(1, 1) == 33
