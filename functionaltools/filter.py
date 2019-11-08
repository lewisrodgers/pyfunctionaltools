import __builtin__

from functionaltools import curry


@curry
def filter(fn, xs):
    try:
        _ = iter(xs)
    except TypeError:
        xs = []
    return __builtin__.filter(fn, xs)