from functionaltools import pipe, inc, head


def test_pipe():
    assert pipe(head, inc)([41, 2, 3]) == 42
