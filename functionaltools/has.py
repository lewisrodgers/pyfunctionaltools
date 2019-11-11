from curry import curry


@curry
def has(p, ps):
    try:
        _ = iter(ps)
    except TypeError:
        ps = {}
    return p in ps