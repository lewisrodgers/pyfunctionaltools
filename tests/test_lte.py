from functionaltools import lte


def test_lte():
    five = lte(5)
    assert five(6) == False
    assert five(5) == True
    assert five(4) == True