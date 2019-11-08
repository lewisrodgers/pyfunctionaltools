from functionaltools import apply


def test_apply():
    uppercase = apply(lambda x: x.upper())
    assert uppercase(["a", "b"]) == ["A", "B"]