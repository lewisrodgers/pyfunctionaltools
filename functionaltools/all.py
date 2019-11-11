import __builtin__

from curry import curry
from map import map


@curry
def all(f, lst):
    """Returns `true` if all elements of the list match the predicate, `false` if there are any that don't.
    
    Args:
        f (function): The predicate function.
        lst (list): The list to consider.
    
    Returns:
        bool: `true` if the predicate is satisfied by every element, `false` otherwise.
    """
    return __builtin__.all(map(f, lst))