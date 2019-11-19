from .curry import curry


@curry
def prop(p, ps):
    """Returns a function that when supplied an object returns the indicated property of that object, if it exists.
        
    Args:
        p (str): The property name or array index
        ps (dict): The properties to query

    Returns:
        The value at `ps[p]`
    """
    return ps.get(p)