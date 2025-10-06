def double(x):
    print("**", x, "=>", x * 2, "**")
    return 2 * x


m = map(double, range(3, 7))
f = lambda y: y >= 10
t = filter(f, m)
print(next(t))
print(next(t))
