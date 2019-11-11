import pytest
from functionaltools import T, add, apply, const, identity, if_else


# @pytest.mark.skip
def test_apply():
    foo = apply(if_else, [T, const("hi"), identity])
    assert foo("bye") == "hi"

# @pytest.mark.skip
def test_apply2():
    assert apply(add, [1, 2]) == 3
