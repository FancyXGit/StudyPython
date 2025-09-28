"""Examples for functions"""


def myDivide(n, d=2):
    """Return devide results"""
    return n // d, n % d


a, b = myDivide(11, 3)
c, d = myDivide(19)
print(f"a = {a}, b = {b}, c = {c}, d = {d}")
