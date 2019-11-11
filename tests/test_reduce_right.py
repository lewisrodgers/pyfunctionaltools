import pytest
from functionaltools import reduce_right


@pytest.fixture
def list_a():
    return ["a", "b", "c"]


def test_reduce(list_a):
    sum = reduce_right(lambda a, b: a + b)
    assert sum(list_a) == "cba"


def test_reduce_init(list_a):
    """Should start with d."""
    sum = reduce_right(lambda a, b: a + b, init="d")
    assert sum(list_a) == "dcba"