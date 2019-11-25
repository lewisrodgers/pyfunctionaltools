import builtins

from .curry import curry


@curry
def filter(f, itr):
    try:
        _ = iter(itr)
    except TypeError:
        itr = []
    return builtins.filter(f, itr)