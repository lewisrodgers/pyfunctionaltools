import __builtin__

from add import add
from curry import curry
from dec import dec
from head import head
from inc import inc
from join import join
from join_with import join_with
from lowercase import lowercase
from multiply import multiply
from pipe import pipe
from product import product
from reduce import reduce
from split import split
from split_with import split_with
from sum import sum
from tail import tail
from tap import tap

# @curry
# def flatten(xs):
#     # TODO: test me
#     return reduce(lambda z, y: z + y, [])


# @curry
# def dedupe(xs):
#     # TODO: test me
#     return list(set(xs))




# @curry
# def map(fn, xs):
#     try:
#         _ = iter(xs)
#     except TypeError:
#         xs = []
#     return __builtin__.map(fn, xs)


# @curry
# def filter(fn, xs):
#     # TODO: test me
#     try:
#         _ = iter(xs)
#     except TypeError:
#         xs = []
#     return __builtin__.filter(fn, xs)


# @curry
# def prop(prop, props={}):
#     return props.get(prop)


# @curry
# def equals(a, b):
#     return a == b


# @curry
# def gt(a, b):
#     return a > b


# @curry
# def notEquals(a, b):
#     return complement(equals(a, b))
    

# @curry
# def complement(x):
#     return not x


# @curry
# def ifElse(condition, onTrue, onFalse, xs):
#     return onTrue(xs) if condition(xs) else onFalse(xs)


# @curry
# def any(f, xs):
#     return __builtin__.any(f(x) for x in xs)


# @curry
# def all(f, xs):
#     return __builtin__.all(f(x) for x in xs)


# @curry
# def fork(accumulator, condition, xs):
#     """Process a collection into two collections.
    
#     Args:
#         accumulator (list): You're splitting a list into two, so your initial
#             containers should be something like a 2 dimensional array.
#         condition (function): Truth-y goes into 1st container and false-y
#             goes into 2nd container.
#         xs (list): original list
    
#     Returns:
#         (collection): collections within a collection
#     """
#     @curry
#     def forker(condition, acc, x):
#         print(x)
#         if condition(x):
#             acc[0].append(x)  
#         else:
#             acc[1].append(x)                
#         return acc
#     return reduce(forker(condition), accumulator)(xs)


# @curry
# def compliance(condition, xs):
#     return fork(([],[]), condition, xs)


# @curry
# def elem(x, xs):
#     return x in xs


# @curry
# def has(prop, props):
#     try:
#         _ = iter(props)
#     except TypeError:
#         props = {}
#     return prop in props


# @curry
# def both(a, b, xs):
#     return a(xs) and b(xs)
