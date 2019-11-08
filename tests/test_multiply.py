from functionaltools import multiply


def test_multiply():
    assert multiply(2, 4) == 8


def test_multiply_partial():
    multi2 = multiply(2)
    assert multi2(4) == 8