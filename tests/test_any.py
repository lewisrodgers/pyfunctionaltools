import pytest
from functionaltools import any, equals


class TestAny: 
    @pytest.mark.parametrize(
        "pred, input, expected", [
            ("a", ["a","b","c"], True),
            (1, [1,2,3], True),
            (1, (1,2,3), True),
            (1, {1,2,3}, True)
        ]
    )
    def test_truthy(self, pred, input, expected):
        assert any(equals(pred), input) == expected

    @pytest.mark.parametrize(
        "pred, input, expected", [
            ("d", ["a","b","c"], False),
            (4, [1,2,3], False),
            (4, (1,2,3), False),
            (4, {1,2,3}, False)
        ]
    )
    def test_falsey(self, pred, input, expected):
        assert any(equals(pred), input) == expected
