import functools


def reduce_by(fn, init=None):
    def reduce_by_(xs):
        if init is not None:
            return functools.reduce(fn, xs, init)
        return functools.reduce(fn, xs)
    return reduce_by_