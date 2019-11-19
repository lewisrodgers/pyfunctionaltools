from .reduce_right import reduce_right


def compose(*fs):
    def compose_(x):
        return reduce_right(lambda x, f: f(x), init=x)(fs)
    return compose_
