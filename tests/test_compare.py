from functionaltools import compare


def test_compare_strings():
    same_as = compare("abc")
    assert same_as("ab") == False
    assert same_as("acb") == True
    assert same_as("abc") == True


def test_compare_lists():
    same_as = compare([1, 2, 3, "4", {"five": 5}])
    assert same_as([1, 2, 4]) == False
    assert same_as([1, 2, 3, 4]) == False
    assert same_as([1, 2, 3, 4, {"five": 6}]) == False
    assert same_as([1, 2, "4", 3, {"five": 5}]) == True
    assert same_as([1, 2, 3, "4", {"five": 5}]) == True


def test_compare_nested_lists():
    same_as = compare([1, {"one": {"two": [3]}}])
    assert same_as([1, {"one": {"two": [3, 4]}}]) == False