from functionaltools import compose, inc, head


def test_compose():
    assert compose(inc, head)([41, 2, 3]) == 42
