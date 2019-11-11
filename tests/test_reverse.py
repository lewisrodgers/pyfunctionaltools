import pytest
from functionaltools import reverse


def test_reverse_string():
    assert reverse("abc") == "cba"


def test_reverse_list():
    assert reverse([1, 2, 3]) == [3, 2, 1]


def test_reverse_tuple():
    assert reverse((1, 2, 3)) == (3, 2, 1)
