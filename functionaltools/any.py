import builtins

from .curry import curry
from .map import map


@curry
def any(f, lst):
    """Returns `true` if at least one of the elements of the list match the predicate, `false` otherwise.
    
    Args:
        f (function): The predicate function.
        lst (list): The list to consider.
    
    Returns:
        bool: `true` if the predicate is satisfied by at least one element, `false` otherwise.
    """
    return builtins.any(map(f, lst))
