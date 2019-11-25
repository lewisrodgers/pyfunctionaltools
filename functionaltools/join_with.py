from .curry import curry


@curry
def join_with(sep, lst):
    """ Returns a string made by inserting the `separator` between each element and concatenating all the elements into a
    single string.

    Args:
        sep (str, optional): The string used to separate the elements. Defaults to "".
        lst (list): The elements to join into a string. Defaults to [].

    Returns:
        str: The string made by concatenating `lst` with `sep`.
    """
    return sep.join(lst)