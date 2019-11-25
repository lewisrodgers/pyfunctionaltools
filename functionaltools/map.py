import builtins

from .curry import curry


@curry
def map(f, itr):
    try:
        _ = iter(itr)
    except TypeError:
        itr = []
    return builtins.map(f, itr)
