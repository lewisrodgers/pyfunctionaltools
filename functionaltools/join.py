from curry import curry
from join_with import join_with


def join(sep=None):
    if not sep:
        return join_with("")
    return join_with(sep)