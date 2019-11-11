import pytest
from functionaltools import reduce


@pytest.fixture
def list_a():
    return ["a", "b", "c"]


class TestReduce:
    def test_reduce(self, list_a):
        assert reduce(lambda a, b: a + b)(list_a) == "abc"

    def test_init(self, list_a):
        """Should start with z."""
        assert reduce(lambda a, b: a + b, init="z")(list_a) == "zabc"