import pytest
from functionaltools import T, cond, const, equals


# @pytest.mark.skip
def test_cond():
    fn = cond(
        [equals(0), const("water freezes at 0")],
        [equals(100), const("water boils at 100")],
        [T, lambda temp: "nothing special happens at {}".format(temp)]
    )
    assert fn(0) == "water freezes at 0"
    assert fn(100) == "water boils at 100"
    assert fn(50) == "nothing special happens at 50"
