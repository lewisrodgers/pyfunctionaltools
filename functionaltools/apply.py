from .curry import curry
from .reduce import reduce


@curry
def apply(fn, args):
    return fn(*args)
