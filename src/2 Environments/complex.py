def square(x):
    return x * x


def make_adder(n):
    def adder(k):
        return n + k

    return adder


def compose(f, g):
    def h(x):
        return f(g(x))

    return h


compose(square, make_adder(2))(3)
