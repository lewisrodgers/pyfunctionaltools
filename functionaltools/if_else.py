from .curry import curry
from .identity import identity
from .F import F


@curry
def if_else(condition, on_true, on_false, x):
    return on_true(x) if condition(x) else on_false(x)
