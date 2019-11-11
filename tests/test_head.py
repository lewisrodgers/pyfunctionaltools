from functionaltools import head


def test_head_list():
    assert head([1,2,3,4]) == 1


def test_head_string():
    assert head("abcdefg") == "a"