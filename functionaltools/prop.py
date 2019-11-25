from .curry import curry


@curry
def prop(p, dct):
    """Returns a function that when supplied an object returns the indicated property of that object, if it exists.
        
    Args:
        p (str): The property name or array index
        dct (dict): The properties to query

    Returns:
        The value at `dct[p]`
    """
    return dct.get(p)