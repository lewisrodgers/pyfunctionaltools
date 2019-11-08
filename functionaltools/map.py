import __builtin__

from functionaltools import curry


@curry
def map(fn, xs):
    try:
        _ = iter(xs)
    except TypeError:
        xs = []
    return __builtin__.map(fn, xs)
