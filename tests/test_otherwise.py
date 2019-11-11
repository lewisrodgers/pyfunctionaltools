from functionaltools import otherwise, cond, const, equals, pipe, T


def test_otherwise():
    always_true = otherwise(T, const("always true"))
    assert always_true("always") == "always true"
    assert always_true("returns") == "always true"
    assert always_true("always true") == "always true"