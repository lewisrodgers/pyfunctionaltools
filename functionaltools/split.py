from split_with import split_with


def split(sep=None):
    if not sep:
        return split_with(None)
    return split_with(sep)