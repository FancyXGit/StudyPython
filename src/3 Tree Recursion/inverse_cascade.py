def inverse_cascade(n):
    k = len(str(n)) - 1

    def helper(n, k):
        if k == 0:
            print(n)
            return
        temp = n // pow(10, k)
        print(temp)
        helper(n, k - 1)
        print(temp)

    return helper(n, k)


inverse_cascade(1234)

print()


def inverse_cascade_2(n):
    grow(n // 10)
    print(n)
    shrink(n // 10)


def grow(n):
    if n < 10:
        print(n)
        return
    grow(n // 10)
    print(n)


def shrink(n):
    if n < 10:
        print(n)
        return
    print(n)
    shrink(n // 10)


inverse_cascade_2(1234)
