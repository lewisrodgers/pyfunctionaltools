from .curry import curry
from .equals import equals


@curry
def compare(ys, xs):
    print(sorted(xs))
    print(sorted(ys))
    return equals(sorted(ys), sorted(xs))

