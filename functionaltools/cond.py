from append import append
from apply import apply
from identity import identity
from if_else import if_else
from map import map
from pipe import pipe
from reduce import reduce
from reverse import reverse
from head import head
from otherwise import otherwise
from reduce_right import reduce_right


def cond(*conditions):
    partials = map(apply(if_else))
    default_cond = append(pipe(reverse, head, apply(otherwise)))
    nest_ifs = reduce_right(lambda x, f: f(x))
    def cond_(x):
        ifs = pipe(partials, default_cond, nest_ifs)(conditions)
        return ifs(x)
    return cond_

# fs = append(identity, map(apply(if_else), conditions))
# ifs = reduce(lambda a, v: v(a))(reverse(fs))
# return ifs(x)
