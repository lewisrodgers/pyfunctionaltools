from functionaltools import equals


def test_equals():
    assert equals(1, 2) == False
    assert equals("a", "b") == False
    assert equals(1, 1) == True
    assert equals("a", "a") == True


def test_equals_list():
    target = equals([1, 2, "abc"])
    assert target([]) == False
    assert target([1, 2]) == False
    assert target([1, "abc", 2]) == False
    assert target([1, 2, "abc"]) == True


def test_equals_dict():
    target = equals({"one": 1, "two": 2, "three": 3})
    assert target({}) == False
    assert target({"one": 1}) == False
    assert target({"one": 1, "three": 3, "two": 2}) == True
    assert target({"one": 1, "two": 2, "three": 3}) == True