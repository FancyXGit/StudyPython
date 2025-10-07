def a_then_b(a, b):
    yield from a
    yield from b


t = a_then_b([1, 2, 3], [4, 5, 6])

print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))

print()


def count_down(k):
    if k > 0:
        yield k
        yield from count_down(k - 1)


t1 = count_down(3)
print(next(t1))
print(next(t1))
print(next(t1))


def prefixes(s):
    if s:
        yield from prefixes(s[:-1])
        yield s


t2 = prefixes("PYTHON")
print(list(t2))
