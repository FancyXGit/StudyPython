def partitions(n, m):
    if n > 0 and m > 0:
        if n == m:
            yield str(m)
        for p in partitions(n - m, m):
            yield p + " " + str(m)
        yield from partitions(n, m - 1)


s = list(partitions(6, 4))
print(s)
