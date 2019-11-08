from functionaltools import join_with


def test_join_with():
    dot = join_with(".")
    assert dot(["www", "example", "com"]) == "www.example.com"