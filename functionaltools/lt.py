from curry import curry


@curry
def lt(a, b):
    return b < a