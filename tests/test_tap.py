from functionaltools import tap


def test_tap():
    assert tap("a") == "a"