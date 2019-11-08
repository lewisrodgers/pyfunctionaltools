from reduce import reduce
from multiply import multiply


def product(x):
    product = reduce(multiply, init=1)
    return product(x)