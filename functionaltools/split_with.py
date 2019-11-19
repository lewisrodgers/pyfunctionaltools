from .curry import curry


@curry
def split_with(sep, xs):
    """ Returns a string made by inserting the `separator` between each element and concatenating all the elements into a
    single string.

    Args:
        sep (str, int): The string used to separate the elements.
        xs (list): The elements to join into a string.

    Returns:
        list: The string made by concatenating `xs` with `sep`.

    Example:
        dots = split(".")
        dots("www.example.com") #=> ["www", "example", "com"]
    """
    return xs.split(sep)
