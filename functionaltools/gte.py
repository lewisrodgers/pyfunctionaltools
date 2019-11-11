from curry import curry


@curry
def gte(a, b):
    return b >= a