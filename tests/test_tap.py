from functionaltools import tap


def foo(x):
    print("blah {}".format(x))


def test_tap():
    log = tap(foo)
    assert log("a") == "a"