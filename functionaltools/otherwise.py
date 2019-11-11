from identity import identity
from if_else import if_else


def otherwise(condition, on_true):
    return if_else(condition, on_true, identity)
