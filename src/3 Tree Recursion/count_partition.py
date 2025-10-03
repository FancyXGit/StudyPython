def count_partition(n, k):
    if n == 0:
        return 1
    if n < 0 or k == 0:
        return 0
    return count_partition(n - k, k) + count_partition(n, k - 1)


print(count_partition(6, 4))
