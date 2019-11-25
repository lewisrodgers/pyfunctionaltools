import functools


# def reduce(fn, init=None):
#     def reduce_(xs):
#         if init is not None:
#             return functools.reduce(fn, xs, init)
#         return functools.reduce(fn, xs)
#     return reduce_


def reduce(fn, init=None):
    def reduce_(xs):
        if init is not None:
            return functools.reduce(fn, xs, init)
        return functools.reduce(fn, xs)
    return reduce_