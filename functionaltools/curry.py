def curry(x, argc=None):
    if argc is None:
        argc = x.func_code.co_argcount
    def curry_p(*a):
        if len(a) == argc:
            return x(*a)
        def curry_q(*b):
            return x(*(a + b))
        return curry(curry_q, argc - len(a))
    return curry_p