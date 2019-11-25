from timeit import timeit
from functionaltools import map, prop, pluck

def data():
    return [{'name':n} for n in range(10000000)]

def data_iter():
    return ({'name':n} for n in range(1000))

def foo():
    results = []
    for n in data():
        results.append(n.get('name'))
    return results

setup = """
from __main__ import data
from functionaltools import prop
"""

setup2 = """
from __main__ import data
from functionaltools import pluck
"""

setup3 = """
from __main__ import data
from functionaltools import map, prop
"""

# t = timeit("(n.get('name') for n in data())", setup="from __main__ import data", number=1)
# print("get:   {}".format(t))

t = timeit("pluck('name', data())", setup=setup2, number=5)
print("pluck: {}".format(t))

# t = timeit("foo()", setup="from __main__ import foo", number=1)
# print("foo:   {}".format(t))

# t = timeit("(prop('name', n) for n in data())", setup=setup, number=1)
# print("prop:  {}".format(t))

# t = timeit("map(prop, data())", setup=setup3, number=1)
# print("map:   {}".format(t))

# t = timeit("list(map(prop, data()))", setup=setup3, number=1)
# print("list:  {}".format(t))
