from curry import curry


""" Returns a string made by inserting the `separator` between each element and concatenating all the elements into a
single string.

Args:
    sep (str, optional): The string used to separate the elements. Defaults to "".
    xs (list): The elements to join into a string. Defaults to [].

Returns:
    str: The string made by concatenating `xs` with `sep`.
"""
@curry
def join_with(sep, xs):
    return sep.join(xs)