import pytest
from functionaltools import reduce


@pytest.fixture
def list_a():
    return [0, 1, 2, 3, 4]


def test_reducer(list_a):
    sum = reduce(lambda a, b: a + b)
    assert sum(list_a) == 10


def test_with_initial(list_a):
    """Should start with 1."""
    sum = reduce(lambda a, b: a + b, init=1)
    assert sum(list_a) == 11