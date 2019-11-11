from functionaltools import const


def test_const():
    ten = const(10)
    assert ten() == 10