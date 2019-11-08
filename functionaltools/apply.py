from curry import curry


@curry
def apply(fn, xs):
    return map(fn, xs)