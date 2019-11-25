from .curry import curry


def tap(f=None):
    def tap_(x):
        if f is not None:
            f(x)
        else:
            print(">>> {}\n---".format(x))
        return x
    return tap_