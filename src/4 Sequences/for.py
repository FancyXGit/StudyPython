pairs = [[1, 2], [3, 4], [5, 5], [6, 6]]


def find_same_count(pairs):
    same_count = 0
    for x, y in pairs:
        if x == y:
            same_count += 1
    return same_count


print(find_same_count(pairs))

a, b = [100, 200]
print(a, b)
