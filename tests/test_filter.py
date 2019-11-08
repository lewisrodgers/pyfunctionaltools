import pytest
from functionaltools import filter


@pytest.fixture
def predicate():
    return lambda x: x == 1


def test_filter_partial(predicate):
    takeOnes = filter(predicate)
    assert takeOnes([1, 2, 1, 3]) == [1, 1]
