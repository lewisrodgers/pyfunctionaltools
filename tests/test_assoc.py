import pytest

from functionaltools import assoc


def test_assoc():
    dct = {"one": 1}
    assert assoc("two", 2, dct) == {"one": 1, "two": 2}
