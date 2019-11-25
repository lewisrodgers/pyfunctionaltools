from .curry import curry


@curry
def has(p, dct):
    try:
        _ = iter(dct)
    except TypeError:
        dct = {}
    return p in dct