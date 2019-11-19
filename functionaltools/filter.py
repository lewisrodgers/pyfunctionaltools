import builtins

from .curry import curry


@curry
def filter(fn, xs):
    try:
        _ = iter(xs)
    except TypeError:
        xs = []
    return list(builtins.filter(fn, xs))