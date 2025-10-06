bcd = ["b", "c", "d"]
m = map(lambda x: x.upper(), bcd)
b = next(m)
c = next(m)
d = next(m)
print([b, c, d])
print(bcd)
