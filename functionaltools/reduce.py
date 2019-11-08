import functools


def reduce(fn, init=None):
    def f(xs):
        if init is not None:
            return functools.reduce(fn, xs, init)
        return functools.reduce(fn, xs)
    return f