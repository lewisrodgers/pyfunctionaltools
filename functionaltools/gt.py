from .curry import curry


@curry
def gt(a, b):
    return b > a