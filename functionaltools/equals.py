from curry import curry


@curry
def equals(a, b):
    return a == b