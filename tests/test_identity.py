from functionaltools import identity


def test_identity():
    assert identity("abc") == "abc"
    