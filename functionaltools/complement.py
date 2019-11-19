from .curry import curry

@curry
def complement(f, x):
    """Takes a function `f` and returns a function `g` such that if called with the same arguments when `f` returns a 
    "truthy" value, `g` returns `false` and when `f` returns a "falsy" value `g` returns `true`.

    Args:
        f (function)

    Returns:
        The function
    """
    return not f(x)