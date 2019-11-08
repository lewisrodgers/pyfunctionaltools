from functionaltools import join


def test_default():
    default = join()
    assert default(["a", "b", "c"]) == "abc"


def test_space():
    spacer = join(" ")
    assert spacer(["a", "b", "c"]) == "a b c"