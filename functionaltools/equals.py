from curry import curry


@curry
def equals(a, b):
    """Returns `true` if its arguments are equivalent, `false` otherwise. Handles nested collections.

    Args:
        a (*)
        b (*)
    
    Returns:
        bool
    """
    return a == b