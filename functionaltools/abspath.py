import os


def abspath(file):
    return os.path.join(os.path.abspath(""), file)
