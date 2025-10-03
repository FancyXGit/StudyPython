def split(n):
    return n // 10, n % 10


def digit_sum(n):
    if n == 0:
        return 0
    a, b = split(n)
    return digit_sum(a) + b


print(digit_sum(1234))
