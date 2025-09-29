"""Calculate fibonacci array"""


def fibonacci(n):
    """fibonacci array(0 1 1 2 3 …) return n th value"""
    prev = 0
    curr = 1
    k = 0
    if n == 0:
        return 0
    while k < n - 1:
        prev, curr = curr, prev + curr
        k = k + 1
    return curr


print(fibonacci(10))
