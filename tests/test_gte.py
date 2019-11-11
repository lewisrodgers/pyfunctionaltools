from functionaltools import gte


def test_gte():
    five = gte(5)
    assert five(6) == True
    assert five(5) == True
    assert five(4) == False