from functionaltools import split_with


def test_split_with():
    dot = split_with(".")
    assert dot("www.example.com") == ["www", "example", "com"]