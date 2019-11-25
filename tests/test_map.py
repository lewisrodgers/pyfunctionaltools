import pytest
from functionaltools import map


@pytest.fixture
def predicate():
    return lambda x: x + 1


def test_map(predicate):
    addOne = map(predicate)
    results = addOne([1, 2, 3])
    assert list(results) == [2, 3, 4]
