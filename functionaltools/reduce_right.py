import functools
from reverse import reverse


def reduce_right(fn, init=None):
    def reduce_right_(xs):
        xs = reverse(xs)
        if init is not None:
            return functools.reduce(fn, xs, init)
        return functools.reduce(fn, xs)
    return reduce_right_