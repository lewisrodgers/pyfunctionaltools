from curry import curry
from map import map
from prop import prop


"""Returns a new list by plucking the same named property off all objects in the list supplied.

Args:
    p (str): The property name to pluck off of each object.
    xs (list): The list of values to consider.

Returns:
    list: The list of values for the given property.
"""
@curry
def pluck(p, xs):
    return map(prop(p), xs)