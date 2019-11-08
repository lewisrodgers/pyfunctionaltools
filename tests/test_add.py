from functionaltools import add


def test_add():
    assert add(1, 41) == 42


def test_add_partial():
    add1 = add(1)
    assert add1(41) == 42