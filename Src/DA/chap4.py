def vector_add(xs, ys):
    return [x + y for x,y in zip(xs,ys)]

def vector_subtract(xs, ys):
    return [x - y for x,y in zip(xs,ys)]

def vector_sum(vectors):
    sum = vectors[0]
    for ys in vectors[1:]:
        sum = vector_add(sum,ys)
    return sum

def scalar_multiply(v, xs):
    return [v*x for x in xs]

def dot(xs, ys):
    return [x * y for x,y in zip(xs,ys)]


def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))
ch
