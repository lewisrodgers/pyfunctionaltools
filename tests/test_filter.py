import pytest
from functionaltools import filter


@pytest.fixture
def predicate():
    return lambda x: x == 1


def test_filter_partial(predicate):
    takeOnes = filter(predicate)
    results = takeOnes([1, 2, 1, 3])
    assert list(results) == [1, 1]
