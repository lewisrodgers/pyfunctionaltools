from curry import curry


@curry
def append(x, xs):
    xs.append(x)
    return xs
