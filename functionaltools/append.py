from .curry import curry


@curry
def append(x, lst):
    lst.append(x)
    return lst
