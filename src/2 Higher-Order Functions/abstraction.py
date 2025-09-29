"""example for abstraction"""


def array_sum(func, n):
    """return n sum for function func
    \n notice that func's index should start from 0"""
    sum = 0
    for i in range(n):
        sum += func(i)
    return sum


def func1(n):
    """test function"""
    if n == 0:
        return 0
    return n


print(array_sum(func1, 100))
