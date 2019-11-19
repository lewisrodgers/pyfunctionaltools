import builtins

from .curry import curry


@curry
def map(fn, xs):
    try:
        _ = iter(xs)
    except TypeError:
        xs = []
    return list(builtins.map(fn, xs))
