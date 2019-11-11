from curry import curry


@curry
def lte(a, b):
    return b <= a