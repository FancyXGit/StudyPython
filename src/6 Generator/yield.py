def evens(start, end):
    even = start + (start % 2)
    while even < end:
        yield even
        even += 2


t = evens(2, 10)
print(next(t))
print(next(t))
print(next(t))
print(next(t))


def print2():
    yield 1
    yield 2


print()
t1 = print2()
print(next(t1))
print(next(t1))
