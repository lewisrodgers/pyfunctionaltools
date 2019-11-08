from curry import curry
from equals import equals


@curry
def compare(ys, xs):
    return equals(sorted(ys), sorted(xs))

