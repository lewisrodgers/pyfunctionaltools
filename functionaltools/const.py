"""Returns a function that always returns the given value.
    
Args:
    x (*): The value to wrap in a function

Returns:
    A function
"""
def const(x):
    def f(args=None):
        return x
    return f