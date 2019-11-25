import builtins


def open(f):
    def _open(file):
        with builtins.open(file) as fh:
            return f(fh)
    return _open