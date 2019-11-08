import pytest
from functionaltools import map


@pytest.fixture
def predicate():
    return lambda x: x + 1


def test_map(predicate):
    addOne = map(predicate)
    assert addOne([1, 2, 3]) == [2, 3, 4]
