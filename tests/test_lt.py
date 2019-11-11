from functionaltools import lt


def test_lt():
    under_five = lt(5)
    assert under_five(6) == False
    assert under_five(5) == False
    assert under_five(4) == True