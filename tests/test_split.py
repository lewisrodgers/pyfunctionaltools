from functionaltools import split


def test_default():
    default = split()
    assert default("a   b \nc ") == ["a", "b", "c"]


def test_space():
    space = split(" ")
    assert space("a  b \nc ") == ["a", "", "b", "\nc", ""]