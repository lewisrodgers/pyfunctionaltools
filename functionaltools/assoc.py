import copy

from .curry import curry


@curry
def assoc(k, v, dct):
    dct = copy.deepcopy(dct)
    dct[k] = v
    return dct