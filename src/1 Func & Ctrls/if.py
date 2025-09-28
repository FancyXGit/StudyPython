"""if control test"""


def absolute(x):
    """Return the absolute value of x"""
    if x < 0:
        return -x
    elif x == 0:
        return 0
    else:
        return x


print(absolute(-10))
