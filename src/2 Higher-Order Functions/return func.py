"""Generalization"""


def make_adder(n):
    """>>> make_adder(n)(k)\n
    n + k"""

    def adder(k):
        return n + k

    return adder


print(make_adder(10)(20))
