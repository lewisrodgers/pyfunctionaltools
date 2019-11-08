from reduce import reduce


def pipe(*fs):
    def f(x):
        pipeline = reduce(lambda v, f: f(v), init=x)
        return pipeline(fs)
    return f