from .curry import curry
from .map import map
from .prop import prop


@curry
def pluck(p, xs):
    """Returns a new list by plucking the same named property off all objects in the list supplied.

    Args:
        p (str): The property name to pluck off of each object.
        xs (list): The list of values to consider.

    Returns:
        list: The list of values for the given property.
    """
    return map(prop(p), xs)

# @curry
# def pluck(p, itr):
#     """Returns a new list by plucking the same named property off all objects in the list supplied.

#     Args:
#         p (str): The property name to pluck off of each object.
#         itr (:obj:`iter` of :obj:`dict`): The list to consider.

#     Returns:
#         iter: The list of values for the given property.
#     """
#     return (dct.get(p) for dct in itr)