from .reduce import reduce


def pipe(*fs):
    def pipe_(x):
        return reduce(lambda x, f: f(x), init=x)(fs)
    return pipe_