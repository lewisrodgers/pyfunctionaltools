from functionaltools import equals


def test_num():
    assert equals(1, 1) == True
    assert equals(1, 2) == False


def test_string():
    assert equals("a", "a") == True
    assert equals("a", "b") == False


def test_equals_list():
    assert equals(list(), list()) == True
    assert equals(list(), [1]) == False


def test_equals_tuple():
    assert equals(tuple(), tuple()) == True
    assert equals(tuple(), (1)) == False


def test_equals_dict():
    assert equals(dict(), dict()) == True
    assert equals(dict(), {"one": 1}) == False


def test_equals_set():
    assert equals(set(), set()) == True
    assert equals(set(), {1}) == False


def test_nested_list():
    nested = equals([1, [2, [{"three": 3}]]])
    assert nested([1, [2, [{"three": 3}]]]) == True
    assert nested([1, [2, [{"three": 3}, {"four": 4}]]]) == False


def test_nested_dict():
    nested = equals({"one": 1, "two": {"three": 3}})
    assert nested({"one": 1, "two": {"three": 3}}) == True
    assert nested({"one": {"two": 2}, "three": 3}) == False