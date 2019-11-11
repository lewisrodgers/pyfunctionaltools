from curry import curry
from identity import identity
from F import F


@curry
def if_else(condition, on_true, on_false, x):
    return on_true(x) if condition(x) else on_false(x)


# @curry
# def if_else(condition, on_true, on_false):
#     def if_else_(val):
#         print(on_false)
#         if condition(val):
#             return on_true(val)
#         return F() if on_false is None else on_false(val)
#     return if_else_